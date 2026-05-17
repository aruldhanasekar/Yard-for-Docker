import asyncio
import os
from dotenv import load_dotenv
import json
import typer

from openai import AsyncOpenAI

from yard.prompt.intent_prompt import SYSTEM_PROMPT
from yard.schema.intent_schema import INTENT_TOOLS

from yard.logger_config import get_logger

logger = get_logger(__name__)

load_dotenv()


def get_openai_client():
    if not os.getenv("OPENAI_API_KEY"):
        typer.echo("OPENAI_API_KEY is not set")
        raise typer.Exit(code=1)

    return AsyncOpenAI(timeout=60)

client = get_openai_client()


async def intent_identifier(intent):
    messages = [{
                    "role": "system", 
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user", 
                    "content": intent
                }]
    
    response = await client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=messages,
        tools=INTENT_TOOLS,
        tool_choice="auto"
)
    
    messages = response.choices[0].message

    if messages.tool_calls:
        tool_call = messages.tool_calls[0]

        task_name = tool_call.function.name 

        arguments = json.loads(
            tool_call.function.arguments
        )

            
        if task_name == "non_docker_request":
            logger.info("Task is not related to Docker")
            return {
                "success" : False,
                "task" : task_name,
                "data" : arguments
            }

        logger.info(f"Task {task_name} Indentified")   
        return {
            "success": True,
            "task": task_name,
            "data": arguments
        }

if __name__ == "__main__":
    print(asyncio.run(intent_identifier("Create a dockerfile for modelai.py from src directory")))
