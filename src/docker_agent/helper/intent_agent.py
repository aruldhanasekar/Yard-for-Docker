import asyncio
import os
from dotenv import load_dotenv

from openai import AsyncOpenAI

from docker_agent.prompt.intent_prompt import SYSTEM_PROMPT

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
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "intent_identifier",
                "strict": True,
                "schema": {
                    "type" : "object",
                    "properties" : {
                        "intent" : {
                            "type" : "string",
                            "enum": [
                                "create_dockerfile",
                                "unrelated_intent"
                            ]
                        },
                        "runnable_file": {
                            "type" : ["array", "null"],
                            "items" : {
                                "type" : "object",
                                "properties": {
                                    "file" : {
                                        "type" : "string"
                                    },
                                    "folder" : {
                                        "type" : "string"
                                    }
                                },
                                "required" : ["file", "folder"],
                                "additionalProperties": False
                            }
                        },
                        "mode" : {
                            "type" : ["string", "null"]
                        },
                        "response" : {
                            "type" : ["string", "null"]
                        }
                    },
                    "required" : ["intent", "runnable_file", "mode", "response"],
                    "additionalProperties": False
                }
            }
        }
)
    
    return response.choices[0].message.content

if __name__ == "__main__":
    print(asyncio.run(intent_identifier("Create a dockerfile for modelai.py from src directory")))
