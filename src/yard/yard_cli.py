import sys
import asyncio
import typer
from typer import Typer, Option, Argument
from typer.core import TyperGroup
from yard.intent_agent import intent_identifier

from yard.console.help_oargs import custom_help
from yard.console.console_ui import console, info, success
from yard.console.error import command_error
from yard.logger_config import get_logger



from yard.tools.create_dockerfile import create_dockerfile
from yard.tools.docker_ignore_file import dockerignore_file


logger = get_logger(__name__)

__version__ = "0.1.5"


class CustomGroup(TyperGroup):
    def get_command(self, ctx, cmd_name):
        rv = super().get_command(ctx, cmd_name)

        if rv is not None:
            return rv
        
        command_error(cmd_name)

        raise typer.Exit(code=1)

def version_callback(value: str):
    if value:
        print(f"yard {__version__}")
        raise typer.Exit()

app = Typer(cls=CustomGroup, 
            # Typer stops decorating exceptions
            pretty_exceptions_enable=False,
            context_settings={
            # To prevent using the typer's default behaviour of "--help" or '-h'
            "help_option_names" : [],
            "ignore_unknown_options": True
            },
            rich_markup_mode=None
        )

@app.callback(invoke_without_command=True)
def yard_agent(
    ctx: typer.Context,
    prompt: str = Argument(""), 
    help: bool = Option(
        False,
        "--help",
        "-h",
        is_eager=True,
    ),
    version: bool = Option(
        False,
        "--version",
        "-v",
        callback=version_callback,
        is_eager=True,
    ),
):  
    # it identifies whether typer misunderstood the optional args as prompt
    if ctx.args or (prompt and prompt.startswith("-")):
        no_option = ctx.args[0] if ctx.args else prompt   
        command_error(no_option)
        raise typer.Exit(code=1)

    if help:
        custom_help()
        raise typer.Exit()
        
    if len(sys.argv) < 2:
        custom_help()
        raise typer.Exit()
    
    
    with console.status(
        "[cyan]Analyzing request[/cyan]"
    ):
        try:
            logger.info("Sending the user message to intent agent")

            result = asyncio.run(intent_identifier(prompt))

        except RuntimeError:
            print("OPENAI_API_KEy is not set")
            raise typer.Exit(code=1)

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