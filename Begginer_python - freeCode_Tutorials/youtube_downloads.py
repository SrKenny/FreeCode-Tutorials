from pytube import YouTube
import os

# Obtém informações do vídeo em um objeto do tipo Youtube
URL = input("Cole a URL: ")
yt = YouTube(URL)

# Define a pasta onde os vídeos serão baixados
pasta_videos = os.getcwd() + os.sep + "videos"

# Recupera a maior resolução disponível para o video
video = yt.streams.get_highest_resolution()

# Realiza o download do vídeo na pasta definida
video.download(output_path=pasta_videos)