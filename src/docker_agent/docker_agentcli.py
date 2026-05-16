import asyncio
import json
import typer
from typer import Typer, Context, Option, Argument
from typer.core import TyperGroup
from docker_agent.console.console_ui import console, info, success
from docker_agent.console.help_oargs import custom_help
from docker_agent.helper.intent_agent import intent_identifier
from docker_agent.console.error import command_error


from docker_agent.tools.create_dockerfile import create_dockerfile
from docker_agent.tools.docker_ignore_file import dockerignore_file


class CustomGroup(TyperGroup):
    def get_command(self, ctx, cmd_name):
        rv = super().get_command(ctx, cmd_name)

        if rv is not None:
            return rv
        
        command_error(cmd_name)

        raise typer.Exit(code=1)

app = Typer(cls=CustomGroup, 
            # Typer stops decorating exceptions
            pretty_exceptions_enable=False,
            context_settings={
            # To prevent using the typer's default behaviour of "--help" or '-h'
            "help_option_names" : []
        })

@app.callback(invoke_without_command=True)
def yard_agent(
    prompt: str = Argument(""), 
    help: bool = Option(
        False,
        "--help",
        "-h",
        is_eager=True,
    ),
):  
    with console.status(
        "[cyan]Analyzing request[/cyan]"
    ):
        if help:
            custom_help()
            raise typer.Exit()
     
        result = asyncio.run(intent_identifier(prompt))

    if result["success"] is True:

        intent = result["data"]
        if result["data"]["task"] == "create_dockerfile":

            success(f"Prepared {result['data']['task']} tasks")

            asyncio.run(create_dockerfile(intent))

        elif result["data"]["task"] == "create_dockerignore":

            success(f"Prepared {result['data']['task']} tasks")

            asyncio.run(dockerignore_file(intent))
    else:
        info(result["data"]["message"])