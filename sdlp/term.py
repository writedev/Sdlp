from typing import Annotated

import typer
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

import sdlp

from .ui.progress_hooks import progress_downloading, spinner_postprocess
from .utils.format import AudioFormat, ImageFormat, VideoFormat

app = typer.Typer()
console = Console(markup=True, emoji=True)

ui_opts = {
    "quiet": True,
    "no_warnings": True,
    "noprogress": True,
    "progress_hooks": [progress_downloading],
    "postprocessor_hooks": [spinner_postprocess],
}


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is not None:
        return

    presentation_text = f"""
[bold underline blue link={sdlp.__repo_link__}]Sdlp[/bold underline blue link] is a downloader based entirely on [bold underline blue link=https://github.com/yt-dlp/yt-dlp]yt-dlp[/bold underline blue link].
It was created to [i]simplify[/i] the use of [bold underline blue link=https://github.com/yt-dlp/yt-dlp]yt-dlp[/bold underline blue link] and the downloading of videos in various formats.
[bold italic]Sdlp[/bold italic] is a diminutive for [bold italic]S[/bold italic]imple yt-[bold italic]dlp[/bold italic].
    """

    presentation_panel = Panel(
        renderable=presentation_text,
        title="Presentation",
        border_style="dim",
        title_align="left",
    )

    console.print(presentation_panel, justify="left")

    console.print(ctx.get_help())


@app.command(help="Download a video using its link")
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


@app.command(help="Download the video thumbnail using the link")
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


@app.command(help="Download the video thumbnail using the link")
def thumbnail(
    url: Annotated[str, typer.Argument()] = "",
    format: Annotated[ImageFormat, typer.Option()] = ImageFormat.PNG,
):
    if not url:
        url = Prompt.ask(
            "[b]Enter the url of your video for transfrom its in audio[/b]",
            console=console,
        )

    try:
        sdlp.download_thumbnails(url=url, format=format.value, extras=(ui_opts))

    except Exception as e:
        print(e)
