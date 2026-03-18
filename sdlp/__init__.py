from pathlib import Path
from typing import Literal

from yt_dlp import YoutubeDL

from .utils.format import VideoFormat
from .utils.types import Output


class Sdlp:
    def __init__(self) -> None:
        self.file_name: str
        self.verbose: bool

    # def download_video(self, url: str, format: VideoFormat = VideoFormat.MP4):
    #     with YoutubeDL() as ydl:  # type: ignore
    #         ydl.download(url)

    #     return True
    def download_video(
        self,
        url: str,
        format: Literal["mp4", "mov", "mkv"],
        no_logs: bool = True,
        file_title: str = "%(title)s",
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

        ydl_opts = format_opts | utils_opts

        with YoutubeDL(ydl_opts) as ydl:  # type: ignore
            info = dict(ydl.extract_info(url))
        return Output(info)
