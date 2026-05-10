from rich import print as rprint
from rich.table import Table
from rich.panel import Panel
from rich import box


def custom_help():
    rprint("[yellow]Usage[/yellow] : [bold yellow]yard[/bold yellow] [ARGS]\n")

    rprint(Panel(renderable="PROMPT       [bold yellow] TEXT [/bold yellow] ",
                     title="Arguments",
                     title_align="left",
                     border_style="dim"
                    ))