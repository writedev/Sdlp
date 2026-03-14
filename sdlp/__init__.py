from .core import app as core_app
import typer
from rich.console import Console
import yt_dlp.version as ydl_version

__version__ = "2.1"

app = typer.Typer(suggest_commands=True)
console = Console()


app.add_typer(core_app)


@app.command()
def version():
    console.print(f"Sdlp version: [b]{__version__}[/b]")
    console.print(f"Sdlp version: [b]{ydl_version.__version__}[/b]")


__main__ = app()

if __name__ == "__main__":
    app()
