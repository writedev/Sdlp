from typing import Annotated

import typer
from rich.console import Console
from rich.prompt import Prompt

import sdlp

from .ui.progress_hooks import progress_downloading, spinner_postprocess
from .utils.format import AudioFormat, VideoFormat

app = typer.Typer()
console = Console(markup=True, emoji=True)

ui_opts = {
    "quiet": True,
    "no_warnings": True,
    "noprogress": True,
    "progress_hooks": [progress_downloading],
    "postprocessor_hooks": [spinner_postprocess],
}


@app.command()
def main():
    print("hello")


@app.command()
def video(
    url: Annotated[str, typer.Argument()] = "",
    format: Annotated[VideoFormat, typer.Option()] = VideoFormat.MP4,
):
    if not url:
        url = Prompt.ask(
            "[b]Enter the url of your video[/b]",
            console=console,
        )

    try:
        sdlp.download_video(url=url, format=format.value, extras=(ui_opts))

    except Exception as e:
        print(e)


@app.command()
def audio(
    url: Annotated[str, typer.Argument()] = "",
    format: Annotated[AudioFormat, typer.Option()] = AudioFormat.MP3,
):
    if not url:
        url = Prompt.ask(
            "[b]Enter the url of your video for transfrom its in audio[/b]",
            console=console,
        )

    try:
        sdlp.download_audio(url=url, format=format.value, extras=(ui_opts))

    except Exception as e:
        print(e)
