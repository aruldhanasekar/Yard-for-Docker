import os
from dotenv import load_dotenv

from openai import AsyncOpenAI

from docker_agent.prompt.intent_prompt import SYSTEM_PROMPT

load_dotenv(".env")


client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))


async def intent_identifier(intent):
    messages = [{
                    "role": "system", 
                    "content": SYSTEM_PROMPT},
                {"role": "user", "content": intent}]
    
    response = await client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=messages,
)
    
    return response.choices[0].message.content
