from typer import Typer
from enum import StrEnum
import typer
from yt_dlp import YoutubeDL
from typing import Annotated, Optional, Literal, Union
import random
from rich.prompt import Prompt

app = Typer()


class AudioFormat(StrEnum):
    MP3 = "mp3"
    WAV = "wav"
    m4a = "M4A"


class VideoFormat(StrEnum):
    MP4 = "mp4"
    MOV = "mov"


class EveryFormat(StrEnum):
    # Audio Format
    MP3 = "mp3"
    WAV = "wav"
    m4a = "M4A"
    # Video Format
    MP4 = "mp4"
    MOV = "mov"


@app.command()
def main():
    pass


@app.command()
def download(
    format: EveryFormat,
    worst: Annotated[bool, typer.Option()] = False,
    random_number: Annotated[bool, typer.Option()] = True,
):
    url: str = Prompt.ask("[b]What is the url ? 🔗 [/b]")
    if not url.startswith("https://"):
        raise typer.Exit()

    if format.value in AudioFormat:
        format_opts = {
            # "format": "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]/b",
            "format": "bestaudio/best",
            "postprocessors": [
                {  # Extract audio using ffmpeg
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": format.value,
                }
            ],
        }

    if format.value in VideoFormat:
        if worst:
            format_opts = {
                # "format": "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]/b",
                "format": "worstvideo*+worstaudio/worst",
                "merge_output_format": format.value,
            }
        else:
            format_opts = {
                # "format": "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]/b",
                "format": "bestvideo*+bestaudio/best",
                "merge_output_format": format.value,
            }

    if random_number:
        title_opts = {
            "outtmpl": f"./%(title)s |[{random.randint(1, 1000)}].%(ext)s",
            "download_archive": None,
            "force_overwrites": True,
        }
    else:
        title_opts = {
            "outtmpl": f"./%(title)s.%(ext)s",
        }

    ydl_opts = format_opts | title_opts

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)


if __name__ == "__main__":
    app()
