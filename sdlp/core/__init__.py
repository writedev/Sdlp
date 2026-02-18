from .video import app as core_video_app
import typer

app = typer.Typer()

app.add_typer(core_video_app)
