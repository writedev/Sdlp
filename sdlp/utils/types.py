from pathlib import Path
from yt_dlp import YoutubeDL


class InfoOutput:
    def __init__(self, pure_info: dict) -> None:
        self.info: dict = pure_info

        self.title: str = pure_info["title"]
        self.id: str = str(pure_info["id"])

        self.original_url: str = pure_info["webpage_url"]

        self.pure_info: dict = pure_info

        self.path = self.get_path()

    def get_path(self) -> Path:
        with YoutubeDL() as ydl:
            path = Path(ydl.prepare_filename(self.pure_info))

        return path


class Output:
    def __init__(self, pure_info: dict) -> None:
        self.pure_info: dict = pure_info

    @property
    def info(self):
        return InfoOutput(self.pure_info)

    def convert_to_mp3(self):
        print("mp3")
