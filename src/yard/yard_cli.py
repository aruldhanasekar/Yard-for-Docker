import asyncio
import json
import typer
from typer import Typer, Context, Option, Argument
from typer.core import TyperGroup
from yard.intent_agent import intent_identifier

from yard.console.help_oargs import custom_help
from yard.console.console_ui import console, info, success
from yard.console.error import command_error
from yard.logger_config import get_logger



from yard.tools.create_dockerfile import create_dockerfile
from yard.tools.docker_ignore_file import dockerignore_file


logger = get_logger(__name__)

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

        logger.info("Sending the user message to intent agent")

        result = asyncio.run(intent_identifier(prompt))

    if result["success"] is True:

        intent = result["data"]

        if result["data"]["task"] == "create_dockerfile":

            success(f"Prepared {result['data']['task']} tasks")
            logger.info("Sending the dockerfile intent to create_dockerfile function")

            asyncio.run(create_dockerfile(intent))

        elif result["data"]["task"] == "create_dockerignore":

            success(f"Prepared {result['data']['task']} tasks")
            logger.info("Sending the ignored files to dockerignore_file function")

            asyncio.run(dockerignore_file(intent))
    else:
        logger.info(f"{result["data"]["message"]}")
        info(result["data"]["message"])