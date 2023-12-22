from pytube.cli import on_progress
from pytube import YouTube

url = "https://www.youtube.com/watch?v=ZTrrc6Ni5eM"
video = YouTube(url)  # add progress bar

stream = video.streams.filter(only_audio=True).first()
stream.download(filename=f"{video.title}.mp3")
