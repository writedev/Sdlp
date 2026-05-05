from yt_dlp import YoutubeDL

with YoutubeDL() as ydl:
    info = ydl.prepare_outtmpl("https://youtu.be/IVdyt2pNxn8?si=z8b7aznXMw3Tmpot")
