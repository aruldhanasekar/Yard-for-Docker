import asyncio
import json

from typer import Typer
from docker_agent.helper.intent_agent import intent_identifier


from docker_agent.tools.create_dockerfile import create_dockerfile



app = Typer()



@app.callback(invoke_without_command=True)
def create(message: str, prod: bool = False):
    if prod: 
        prompt = f"{message}, and the project is intended for production use"

    else:
        prompt = f"{message}, and project is currently in development"
    
    # print(prompt)

    intent = asyncio.run(intent_identifier(prompt))

    intent_dict = json.loads(intent)

    for key, value in intent_dict.items():
        if key == "intent" and value == "create_dockerfile":
            asyncio.run(create_dockerfile(intent_dict))
            break
        else:
            print("Currently I can create only Dockerfiles")