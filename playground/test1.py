from sdlp import Sdlp

video = Sdlp().download_video(
    "https://youtu.be/IVdyt2pNxn8?si=z8b7aznXMw3Tmpot",
    format="mp4",
    file_title="zizidelastreet",
)

print(video.info.path)

# https://youtu.be/IVdyt2pNxn8?si=z8b7aznXMw3Tmpot
