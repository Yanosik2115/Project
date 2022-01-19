from concurrent.futures.thread import ThreadPoolExecutor
from os import close
from tkinter.constants import TRUE
import pyaudio
import wave
import threading
from queue import Queue
from threadpoolctl import ThreadpoolController
from multiprocessing import Process
# from concurrent.futures import ProcessPoolExecutor
# global flag
# flag = False

# def threading(file):
#     global flag
#     thread = threading.Thread(target=AudioFile(file).play)
#     if not flag:
#         thread.start()
#     if flag:
#         thread.start()

class PlayQueue:
    def __init__(self) -> None:
        self.q = Queue()
        self.p = Process
    def threading(self, file):
        self.p.start(target=AudioFile(file).play())
        #self.p.start()
        self.p.join()
        self.p.is_alive()
        print("dupa")
        #self.q.get()
        

class AudioFile:
    chunk = 1024

    def __init__(self, file):
        """Init audio stream"""
        self.wf = wave.open("/home/yanosik2115/Py/Project/SongsWav/" + file, "rb")
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=self.p.get_format_from_width(self.wf.getsampwidth()),
            channels=self.wf.getnchannels(),
            rate=self.wf.getframerate(),
            output=True,
        )

    def play(self):
        """Play entire file"""
        data = self.wf.readframes(self.chunk)
        while data != "":
            self.stream.write(data)
            data = self.wf.readframes(self.chunk)

    def close(self):
        """Graceful shutdown"""
        self.stream.close()
        self.p.terminate()

    # AudioThread_2 = AudioFile(file)

    # t1 = Thread(target=AudioThread_1.play)
    # t2 = Thread(target=AudioThread_1.play)

    # if t1.is_alive:
    #     AudioThread_1.close
    #     t2.start()
    # else:
    #     AudioThread_2.close
    #     t1.start()


# Usage example for pyaudio
