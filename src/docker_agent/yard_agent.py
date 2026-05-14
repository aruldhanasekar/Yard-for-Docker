import os
from dotenv import load_dotenv
import json

from openai import AsyncOpenAI
from docker_agent.prompt.agent_prompt import SYSTEM_PROMPT
from docker_agent.schema.yard_schema import TOOLS


load_dotenv(".env")

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))


async def yard_devops(intent):
    messages = [{
        "role": "system",
        "content": SYSTEM_PROMPT
    },
    {
        "role": "user",
        "content": intent
    }]

    response = await client.chat.completions.create(
        model="gpt-5.4",
        messages=messages,
        tools=TOOLS,
        tool_choice="auto"
        
    )

    message = response.choices[0].message

    if message.tool_calls:
        content = message.tool_calls[0]

        output = json.loads(
            content.function.arguments
        )

        return output


