from pytube import YouTube

link = "https://www.youtube.com/watch?v=0U0L4uT0btQ"
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()
