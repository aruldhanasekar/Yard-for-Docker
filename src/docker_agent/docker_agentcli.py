import asyncio
import json
from typing import Optional, List
import typer
from typer import Typer, Context, Option, Argument
from docker_agent.console.console_api import console
from docker_agent.console.help_oargs import custom_help
from docker_agent.helper.intent_agent import intent_identifier


from docker_agent.tools.create_dockerfile import create_dockerfile



app = Typer(context_settings={
    # To prevent using the typer's default behaviour of "--help" or '-h'
    "help_option_names" : []
})

@app.callback(invoke_without_command=True)
def yard_agent(
    ctx: Context,
    prompt: str = Argument(""), 
    help: bool = Option(
        False,
        "--help",
        "-h",
        is_eager=True,
    ),
):
    if help:
        custom_help()
        raise typer.Exit()
    
  

    with console.status(
        "[bold cyan]Analyzing user requirements..."
    ):
        intent = asyncio.run(intent_identifier(prompt))

    
        intent_dict = json.loads(intent)

    for key, value in intent_dict.items():
        if key == "intent" and value == "create_dockerfile":
            console.print(
                    "[green]✓ Intent analyzed successfully[/green]"
                )
            console.print(
                    "[green]Started creating Dockerfiles[/green]"
                )
            asyncio.run(create_dockerfile(intent_dict))
            break
        else:
            console.print(
                "[green] I can create and write Dockerfiles [/green]"
            )
            break