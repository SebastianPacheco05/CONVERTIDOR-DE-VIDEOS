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


convertir_webm_a_mp4(webm_directory, mp4_directory)
print("Convirtido :D")
