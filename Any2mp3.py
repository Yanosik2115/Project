import os

class Converter:
    def __init__(self, file) -> None:

        LOG_LEVEL = "fatal"
        song_name = file.split("/")[-1]
        song_path = "/home/yanosik2115/Py/Project/Songs/"
        file_base_name = song_name[:-4]
        file_mp3 = song_path + file_base_name + ".mp3"

        os.system(
            'ffmpeg -loglevel %s -i "%s" -acodec mp3 "%s"' % (LOG_LEVEL, file, file_mp3)
        )
