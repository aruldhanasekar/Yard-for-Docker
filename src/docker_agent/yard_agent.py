import os
import json
from logging import WARNING
from dotenv import load_dotenv

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

from docker_agent.logger_config import get_logger
from docker_agent.prompt.agent_prompt import SYSTEM_PROMPT
from docker_agent.schema.yard_schema import TOOLS




logger = get_logger(__name__)
load_dotenv(".env")

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"), timeout=60)


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

