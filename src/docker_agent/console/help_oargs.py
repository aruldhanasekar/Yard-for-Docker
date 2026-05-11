from rich import print as rprint
from rich.panel import Panel
from rich import box


def custom_help():
    rprint("[yellow]Usage[/yellow] : [bold yellow]yard[/bold yellow] [ARGS]\n")

    rprint(Panel(renderable="PROMPT       [bold yellow] TEXT [/bold yellow] ",
                     title="Arguments",
                     title_align="left",
                     border_style="dim"
                    ))
    rprint(Panel(renderable='[bold yellow]yard[/bold yellow] [cyan]"Create a dockerfile for main.py"[cyan]', 
                 title="Example command", 
                 title_align="left", 
                 border_style="white"))