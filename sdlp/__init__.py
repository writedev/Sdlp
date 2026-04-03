__version__ = 2.1

from typing import Literal

from yt_dlp import YoutubeDL

from .utils.format import AudioFormat, ImageFormat, VideoFormat
from .utils.output import Video


def download_video(
    url: str,
    format: Literal["mp4", "mov", "mkv"] = "mp4",
    no_logs: bool = True,
    file_title: str = "%(title)s",
    extras: dict | None = None,
):

    VideoFormat(format)
    # Error with mov because the mov doesn't accept the vp9 codec (google codec)

    if format in ["mov", "mkv"]:
        format_opts = {
            "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
            "merge_output_format": format,
            "postprocessors": [
                {
                    "key": "FFmpegVideoRemuxer",
                    "preferedformat": format,
                }
            ],
            "outtmpl": "%(id)s.%(ext)s",
        }
    else:
        format_opts = {
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": format,
        }

    utils_opts = {"quiet": no_logs, "outtmpl": f"{file_title}.%(ext)s"}

    if not extras:
        extras = {}

    ydl_opts = format_opts | utils_opts | extras

    try:
        with YoutubeDL(ydl_opts) as ydl:
            extract_info = dict(ydl.extract_info(url, download=True))

        return Video(extract_info)

    except Exception as e:
        print(e)


def download_audio(
    url: str,
    format: Literal["mp3", "wav", "m4a"] = "mp3",
    no_logs: bool = True,
    file_title: str = "%(title)s",
    extras: dict | None = None,
):

    AudioFormat(format)

    format_opts = {
        # "format": "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]/b",
        "format": "worstvideo+*bestaudio/best",
        "postprocessors": [
            {  # Extract audio using ffmpeg
                "key": "FFmpegExtractAudio",
                "preferredcodec": format,
            }
        ],
    }

    utils_opts = {"quiet": no_logs, "outtmpl": f"{file_title}.%(ext)s"}

    if not extras:
        extras = {}

    ydl_opts = format_opts | utils_opts | extras

    try:
        with YoutubeDL(ydl_opts) as ydl:
            extract_info = dict(ydl.extract_info(url, download=True))

        return Video(extract_info)

    except Exception as e:
        print(e)


def download_thumbnails(
    url: str,
    format: Literal[
        "png",
        "jpg",
    ] = "png",
    no_logs: bool = True,
    file_title: str = "%(title)s",
    extras: dict | None = None,
):

    ImageFormat(format)

    image_opts = {
        "writethumbnail": True,
        "skip_download": True,
        "postprocessors": [
            {
                "key": "FFmpegThumbnailsConvertor",
                "format": format,  # Format cible
                "when": "before_dl",  # Optionnel, force le traitement
            }
        ],
    }

    utils_opts = {"quiet": no_logs, "outtmpl": f"{file_title}.%(ext)s"}

    ydl_opts = image_opts | utils_opts

    try:
        with YoutubeDL(ydl_opts) as ydl:
            extract_info = dict(ydl.extract_info(url, download=True))

        return Video(extract_info)

    except Exception as e:
        print(e)
