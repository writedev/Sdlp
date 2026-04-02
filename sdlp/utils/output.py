from pathlib import Path

from yt_dlp import YoutubeDL


class InfoOutput:
    def __init__(self, pure_info: dict) -> None:
        self.pure_info: dict = pure_info

        self.title: str = pure_info.get("title")

        self.id: str = str(pure_info.get("id"))

        self.original_url: str = pure_info.get("webpage_url")

        self.author: str | None = pure_info.get("uploader")

        self.author_id: str | None = str(pure_info.get("uploader_id"))

        self.duration: int | None = int(pure_info.get("duration"))

        self.path = self.get_path()

    def get_path(self) -> Path:
        with YoutubeDL() as ydl:
            path = Path(ydl.prepare_filename(self.pure_info))

        return path


class Output:
    def __init__(self, pure_info: dict) -> None:
        # self.pure_info: dict = pure_info
        self.__pure_info__ = pure_info
        pass

    @property
    def info(self) -> InfoOutput:
        return InfoOutput(self.__pure_info__)

    def convert_to_mp3(self):
        print("mp3")
