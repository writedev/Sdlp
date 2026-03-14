import typer

from .audio import app as core_audio_app
from .thumbnails import app as core_thumbnails_app
from .video import app as core_video_app

app = typer.Typer()

app.add_typer(core_video_app)
app.add_typer(core_audio_app)
app.add_typer(core_thumbnails_app)
