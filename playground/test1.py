import sdlp
from sdlp.ui.progress_hooks import progress_downloading

video = sdlp.download_audio(
    "https://youtu.be/57C13H0BnnU?si=h_mr2Ajx7snXcHV5",
    format="wav",
    extras={
        "quiet": True,
        "no_warnings": True,
        "noprogress": True,
        "progress_hooks": [progress_downloading],
    },
)

# print(video.info.pure_info)

# https://youtu.be/IVdyt2pNxn8?si=z8b7aznXMw3Tmpot
