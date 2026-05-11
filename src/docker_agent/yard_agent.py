import os
from dotenv import load_dotenv


from openai import AsyncOpenAI
from docker_agent.prompt.agent_prompt import SYSTEM_PROMPT


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
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "yard_response",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "dockerfiles": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "dockerfile_name" : {
                                        "type" : "string"
                                    },
                                    "docker_instructions": {
                                        "type" : "string"
                                    }
                                },
                                "required" : ["dockerfile_name", "docker_instructions"],
                                "additionalProperties": False
                            }
                        }
                    },
                    "required" : ["dockerfiles"],
                    "additionalProperties": False
                }

            }
        }
    )

    return response.choices[0].message.content

