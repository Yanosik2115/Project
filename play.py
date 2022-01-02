import pyaudio
import wave
from threading import *
from threadpoolctl import ThreadpoolController

controller = ThreadpoolController()

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



def threading(file):
    
    AudioThread_1 = AudioFile(file)
    AudioThread_2 = AudioFile(file)

    t1 = Thread(target=AudioThread_1.play)
    t2 = Thread(target=AudioThread_1.play)
    
    if t1.is_alive:
        AudioThread_1.close
        t2.start()
    else:
        AudioThread_2.close
        t1.start()


# Usage example for pyaudio
