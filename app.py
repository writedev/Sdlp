from typer import Typer
from enum import StrEnum
import typer
from yt_dlp import YoutubeDL
from typing import Annotated
import random
from rich.prompt import Prompt, Confirm
from rich.console import Console

app = Typer()
console = Console()


class AudioFormat(StrEnum):
    MP3 = "mp3"
    WAV = "wav"
    m4a = "M4A"


class VideoFormat(StrEnum):
    MP4 = "mp4"
    MOV = "mov"
    MKV = "mkv"


class EveryFormat(StrEnum):
    # Audio Format
    MP3 = "mp3"
    WAV = "wav"
    M4A = "m4a"
    # Video Format
    MP4 = "mp4"
    MOV = "mov"
    MKV = "mkv"


re_encode_opts = {
    "postprocessor_args": {
        "ffmpeg": [
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            "-profile:v",
            "high",
            "-level",
            "4.2",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
        ]
    },
}


@app.command()
def main():
    pass


@app.command()
def download(
    format: EveryFormat,
    file_name: Annotated[
        str, typer.Option(help="Choose file folder name")
    ] = "%(title)s",
    worst: Annotated[bool, typer.Option(help="Get the worst quality video")] = False,
    random_number: Annotated[
        bool, typer.Option(help="Remove the random number in the end folder name")
    ] = True,
):

    url: str = Prompt.ask("[b]What is the url ? 🔗 [/b]")
    if not url.startswith("https://"):
        raise typer.Exit()

    if format.value in AudioFormat:
        format_opts = {
            # "format": "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]/b",
            "format": "worstvideo+*bestaudio/best",
            "postprocessors": [
                {  # Extract audio using ffmpeg
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": format.value,
                }
            ],
        }

    if format.value in VideoFormat:
        if not worst:
            format_opts = {
                "format": "bestvideo+bestaudio/best",
                "merge_output_format": format.value,
            }
        else:
            format_opts = {
                # "format": "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]/b",
                "format": "worstvideo*+worstaudio/worst",
                "merge_output_format": format.value,
            }

        if format.value == "mov" or format.value == "mkv":
            format_confirmation = Confirm.ask(
                "[bold red] Are you sure you want to use mov or mkv because this will require re encored entire video and will take time and performance ? [/bold red]"
            )

            if not format_confirmation:
                console.print("Good decision to save time.")
                raise typer.Exit()

            format_opts = format_opts | re_encode_opts  # Add recoding options

    if random_number:
        title_opts = {
            "outtmpl": f"./{file_name} |[{random.randint(1, 1000)}].%(ext)s",
            "download_archive": None,
            "force_overwrites": True,
        }
    else:
        title_opts = {
            "outtmpl": f"./{file_name}.%(ext)s",
        }

    ydl_opts = format_opts | title_opts  # type: ignore

    with YoutubeDL(ydl_opts) as ydl:  # type: ignore
        ydl.download(url)


if __name__ == "__main__":
    app()
