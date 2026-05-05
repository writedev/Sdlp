import os
from pathlib import Path

from yt_dlp import YoutubeDL


class VideoInfo:
    def __init__(self, pure_info: dict) -> None:
        self.pure_info: dict = pure_info

        self.title: str = pure_info.get("title")

        self.id: str = str(pure_info.get("id"))

        self.original_url: str = pure_info.get("webpage_url")

        self.author: str | None = pure_info.get("uploader")

        self.author_id: str | None = str(pure_info.get("uploader_id"))

        self.duration: int | None = int(pure_info.get("duration"))


class Video:
    def __init__(self, pure_info: dict) -> None:
        # self.pure_info: dict = pure_info
        self.__pure_info__ = pure_info

        self.path = Path()

    @property
    def info(self) -> VideoInfo:
        return VideoInfo(self.__pure_info__)

    def get_path(self) -> Path:
        with YoutubeDL() as ydl:
            path = ydl.prepare_filename(self.__pure_info__)

            path = os.path.splitext(path)[0] + "." + self.__pure_info__["ext"]

        # path = Path(self.__pure_info__["requested_downloads"][0]["filepath"].)

        return Path(path)
