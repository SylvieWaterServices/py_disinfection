"""Console script for py_disinfection."""
import py_disinfection

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for py_disinfection."""
    console.print("Replace this message by putting your code into "
               "py_disinfection.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
