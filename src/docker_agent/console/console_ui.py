from rich.console import Console


console = Console()

def success(message: str) -> None:
    console.print(f"[green]✓{message}[/green]")

def info(message: str) -> None:
    console.print(f"[cyan]{message}[/cyan]")