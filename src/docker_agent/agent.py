import os
from dotenv import load_dotenv


from openai import AsyncOpenAI
from docker_agent.prompt.agent_prompt import SYSTEM_PROMPT




load_dotenv(".env")

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))


async def devops_agent(intent):
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
        messages=messages
    )

    return response.choices[0].message.content

