from .core import app as core_app
import typer

__version__ = "2.1"

app = typer.Typer(suggest_commands=True)

app.add_typer(core_app)

if __name__ == "__main__":
    app()
