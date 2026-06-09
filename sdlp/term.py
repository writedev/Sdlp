from pathlib import Path
from typing import Annotated

import typer
import yt_dlp.version
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


def downloaded_console_msg(path: Path) -> None:
    """The msg when the downloading is finished"""

    return console.print(
        f"[bright_green bold]The downloading is finished :sparkles: -> [link={path.resolve().as_uri()}]Click here to open[/link][/bright_green bold]"
    )


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    version: Annotated[
        bool,
        typer.Option(help="Display the version of Sdlp and yt-dlp"),
    ] = False,
):
    if ctx.invoked_subcommand is not None:
        return

    if version:
        return console.print(f"""
Sdlp version: [bold]{sdlp.__version__}[/bold]
yt-dlp version: [bold]{yt_dlp.version.__version__}[/bold]
""")

    ###############################
    # Presentation text / message #
    ###############################

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


@app.command("video",help="Download a video using its link")
@app.command("v", hidden=True)
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
        video = sdlp.download_video(url=url, format=format.value, extras=(ui_opts))

        downloaded_console_msg(video.path)

    except Exception as e:
        print(e)


@app.command("audio",help="Download the video thumbnail using the link")
@app.command("a", hidden=True)
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
        video = sdlp.download_audio(url=url, format=format.value, extras=(ui_opts))

        downloaded_console_msg(video.path)

    except Exception as e:
        print(e)


@app.command("thumbnail", help="Download the video thumbnail using the link")
@app.command("t", hidden=True)
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
        video = sdlp.download_thumbnail(url=url, format=format.value, extras=(ui_opts))

        downloaded_console_msg(video.path)

    except Exception as e:
        print(e)
