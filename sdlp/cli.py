import typer
import sdlp
from rich.console import Console


app = typer.Typer()
console = Console()


@app.command()
def video(url: str | None):
    sdlp.download_video(url)

    console.print("Finish !")
