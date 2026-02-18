from enum import StrEnum


class AudioFormat(StrEnum):
    MP3 = "mp3"
    WAV = "wav"
    M4A = "m4a"


class VideoFormat(StrEnum):
    MP4 = "mp4"
    MOV = "mov"
    MKV = "mkv"
