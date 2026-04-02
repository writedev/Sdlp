import sdlp
from sdlp.ui.progress_hooks import progress_downloading

video = sdlp.download_audio(
    "https://youtu.be/IVdyt2pNxn8?si=z8b7aznXMw3Tmpot",
    format="wav",
    extras={
        "quiet": True,
        "no_warnings": True,
        "noprogress": True,
        "progress_hooks": [progress_downloading],
    },
)


print(video)

print(video.info.author)
print(video.info.author_id)
print(video.info.duration)
print(video.info.path)
# print(video.info.pure_info)

# https://youtu.be/IVdyt2pNxn8?si=z8b7aznXMw3Tmpot
