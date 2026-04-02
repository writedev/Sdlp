import sdlp
from sdlp.ui.progress_hooks import progress_downloading

video = sdlp.download_video(
    "https://youtu.be/IVdyt2pNxn8?si=z8b7aznXMw3Tmpot",
    format="mp4",
    # extras={
    #     "quiet": True,
    #     "no_warnings": True,
    #     "noprogress": True,
    #     "progress_hooks": [progress_downloading],
    # },
    # extras={
    #     # "format": "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]/b",
    #     "format": "worstvideo+*bestaudio/best",
    #     "postprocessors": [
    #         {  # Extract audio using ffmpeg
    #             "key": "FFmpegExtractAudio",
    #             "preferredcodec": "wav",
    #         }
    #     ],
    # },
)


print(video)
print(video.path)

print(video.info.author)
print(video.info.author_id)
print(video.info.duration)
print(video.info)
# print(video.info.pure_info)

# https://youtu.be/IVdyt2pNxn8?si=z8b7aznXMw3Tmpot
