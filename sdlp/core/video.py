import typer
from ..utils.format import VideoFormat
from typing import Annotated
from rich.prompt import Prompt, Confirm
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def video(
    format: VideoFormat,
    file_name: Annotated[
        str,
        typer.Option(
            help="Choose file folder name (default is the title of the video)"
        ),
    ] = "%(title)s",
    worst: Annotated[bool, typer.Option(help="Get the worst quality video")] = False,
    random_number: Annotated[
        bool,
        typer.Option(
            help="Remove the random number in the end folder name (exemple: |[000])"
        ),
    ] = True,
    verbose: Annotated[bool, typer.Option(help="See every logs of yt-dlp")] = False,
    url: Annotated[str, typer.Option(help="Give the URL")] = "",
    simulate: Annotated[
        bool, typer.Option(help="For test but dont download video")
    ] = False,
):
    if not url:
        url = Prompt.ask("[b]Give the url 🔗 [/b]")

    if not url.startswith("https://"):
        console.print(
            "[bold red]Please retry the command with a direct url.[/bold red]"
        )

    if worst:
        # quality opts (worst quality)

        format_opts = {
            "format": "worstvideo*+worstaudio/worst",
            "merge_output_format": format.value,
        }
    else:
        # quality opts (best quality)

        format_opts = {
            "format": "worstvideo*+worstaudio/worst",
            "merge_output_format": format.value,
        }

    if format.value in ["mkv", "mov"]:
        format_confirmation = Confirm.ask(
            "[bold red] This is a format who take time and performance. Are you sure to continue ?"
        )

        if not format_confirmation:
            console.print("Good decision.")
            raise typer.Exit()

        # Re encode opts

        format_opts = format_opts | {
            "postprocessors": [
                {
                    "key": "FFmpegVideoConvertor",
                    "preferedformat": format.value,
                }
            ]
        }
