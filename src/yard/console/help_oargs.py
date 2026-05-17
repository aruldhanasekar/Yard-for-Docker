from rich.panel import Panel
from rich import print as rprint


def custom_help():
    rprint("[bold yellow]Usage:[/bold yellow] [cyan]yard[/cyan] [white]<prompt>[/white]\n")

    rprint(
        Panel(
            renderable=(
                "[bold cyan]PROMPT[/bold cyan]\n"
                "Describe the task you want the agent to perform.\n\n"
                "[dim]The agent analyzes your request and generates the required project files automatically.[/dim]"
            ),
            title="Arguments",
            title_align="left",
            border_style="dim"
        )
    )

    rprint(
        Panel(
            renderable=(
                "[bold cyan]--help[/bold cyan]      [white]Show this message and exit[/white]\n" \
                "[bold cyan]-h[/bold cyan]          [white]Show this message and exit[/white]"
            ),
            title="Options",
            title_align="left",
            border_style="dim"
        )
    )

    rprint(
        Panel(
            renderable=(
                "[white]Supported Tasks[/white]\n\n"
                "• Create Dockerfile\n"
                "• Create .dockerignore\n"
            ),
            title="Capabilities",
            title_align="left",
            border_style="yellow"
        )
    )

    rprint(
        Panel(
            renderable=(
                '[bold yellow]yard[/bold yellow] '
                '[cyan]"Create a Dockerfile for main.py"[/cyan]\n\n'
                '[bold yellow]yard[/bold yellow] '
                '[cyan]"Create a .dockerignore file and add the files and folders that should be ignored"[/cyan]'
            ),
            title="Examples",
            title_align="left",
            border_style="white"
        )
    )