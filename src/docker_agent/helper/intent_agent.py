import asyncio
import os
from dotenv import load_dotenv
import json

from openai import AsyncOpenAI

from docker_agent.prompt.intent_prompt import SYSTEM_PROMPT
from docker_agent.schema.intent_schema import INTENT_TOOLS

load_dotenv(".env")


client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))


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
            return {
                "success" : False,
                "task" : task_name,
                "data" : arguments
            }
           
        return {
            "success": True,
            "task": task_name,
            "data": arguments
        }

if __name__ == "__main__":
    print(asyncio.run(intent_identifier("Create a dockerfile for modelai.py from src directory")))
