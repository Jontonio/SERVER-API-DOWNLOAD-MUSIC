
from pytube import YouTube
import os

def downloadMP3(url:str):
    try:
        yt = YouTube(url)

        # stract only mp3
        video = yt.streams.filter(only_audio=True).first()
        # download the file 
        out_file = video.download(output_path='./downloads')
        # save the file 
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        # result of success 
        return yt.title + " has been successfully downloaded."
    except NameError:
        return "Ocurrio un error al descargar mp3"