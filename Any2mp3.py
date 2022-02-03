import os
import sys


class Converter:
    def __init__(self, file) -> None:
        self.file_dir = file
        self.format = self.file_dir.split("/")[-1]
        self.song_path = "/Songs/"

    def wmatmp3():
        pass

    def wav2mp3(self):
        LOG_LEVEL = "fatal"
        path = sys.argv[0]
        print(self.file_dir)
        file_base_name = self.file_dir[:-4]
        file_wma = os.path.join(self.file_dir, "%s.wma" % file_base_name)
        file_mp3 = os.path.join(self.song_path, "%s.mp3" % file_base_name)
        os.system(
            'ffmpeg -loglevel %s -i "%s" -acodec mp3 "%s"'
            % (LOG_LEVEL, file_wma, file_mp3)
        )


# if len(sys.argv) != 2:
#     sys.exit('Missing input path!')



# if not os.path.isdir(path):
#     sys.exit('Incorrect input path!')

# items = os.listdir(path)
