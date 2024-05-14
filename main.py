# pip install moviepy
# pip install pytube

import os
from pytube import YouTube
import shutil
from moviepy.editor import VideoFileClip

def convertir_webm_a_mp4(webm_directory, mp4_directory):
    for filename in os.listdir(webm_directory):
      if filename.endswith(".webm"):
          webm_path = os.path.join(webm_directory, filename)
          mp4_path = os.path.join(mp4_directory, filename.replace(".webm", ".mp4"))
          if not os.path.exists(mp4_path):
            video = VideoFileClip(webm_path)
            video.write_videofile(mp4_path)
            
webm_directory = "./videos"
mp4_directory = "./videos_convertidos"

def descargar_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        ruta_descarga = os.path.join(os.getcwd(), "videos_descargados")
        if not os.path.exists(ruta_descarga):
            os.makedirs(ruta_descarga)
        video.download(ruta_descarga)
        print("Descarga completada! El video se ha guardado en:", ruta_descarga)
    except Exception as e:
        print("Error durante la descarga:", e)

if __name__ == "__main__":
    url = input("Ingresa la URL del video de YouTube que deseas descargar: ")
#     descargar_video(url)

convertir_webm_a_mp4(webm_directory, mp4_directory)

