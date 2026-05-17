from rich import print as rprint
from rich.panel import Panel


def command_error(cmd):
    rprint("[yellow]Usage:[/yellow] yard [PROMPT]")
    rprint(Panel(renderable=f"No such '{cmd}' command",
                 title="Error",
                 title_align="left",
                 border_style="red"
                 ))
    