import os
import json
from logging import WARNING
from dotenv import load_dotenv
import typer

from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
    retry_if_exception_type,
    before_sleep_log
)
from openai import AsyncOpenAI
from openai import (
    APIConnectionError,
    APITimeoutError,
    RateLimitError,
    InternalServerError,
)

from yard.logger_config import get_logger
from yard.prompt.agent_prompt import SYSTEM_PROMPT
from yard.schema.yard_schema import TOOLS
from yard.console.console_ui import error



logger = get_logger(__name__)
load_dotenv()


def get_openai_client():
    if not os.getenv("OPENAI_API_KEY"):
        typer.echo("OPENAI_API_KEY is not set")
        raise typer.Exit(code=1)

    return AsyncOpenAI(timeout=60)

client = get_openai_client()


@retry(
        retry=retry_if_exception_type((
            APIConnectionError,
            APITimeoutError,
            RateLimitError,
            InternalServerError,
        )),
        wait=wait_random_exponential(
            multiplier=1,
            max=60,
        ),
        stop=stop_after_attempt(8),
        before_sleep=before_sleep_log(
            logger,
            WARNING
        ),
        reraise=True
)
async def yard_devops(intent):
    messages = [{
        "role": "system",
        "content": SYSTEM_PROMPT
    },
    {
        "role": "user",
        "content": intent
    }]

    logger.info("Send OpenAI request")
    response = await client.chat.completions.create(
        model="gpt-5.4",
        messages=messages,
        tools=TOOLS,
        tool_choice="auto"
            
    )

    logger.info("OpenAI response received")
    message = response.choices[0].message

    if message.tool_calls:
        content = message.tool_calls[0]

        output = json.loads(
            content.function.arguments
            )

        logger.info("Tool call parsed successfully")
        return output
    
    return None

