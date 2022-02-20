from black import TRANSFORMED_MAGICS
import pydub 
import numpy as np
import matplotlib.pyplot as plt
from mutagen.mp3 import MP3

def get_window():
    pass

def read(f, normalized=True):
    """MP3 to numpy array"""
    a = pydub.AudioSegment.from_mp3(f)
    y = np.array(a.get_array_of_samples())
    if a.channels == 2:
        y = y.reshape((-1, 2))
    if normalized:
        return a.frame_rate, np.float32(y) / 2**15
    else:
        return a.frame_rate, y

sr, x = read('./Songs/01 Dwa Trzynas cie.mp3')

song = MP3('./Songs/01 Dwa Trzynas cie.mp3')
print(song.info.length)

# w = np.fft.rfft(x)

# freqs = np.fft.rfftfreq(len(x))

# for coef, freq in zip(w, freqs):
#     if coef:
#         print('{c:>6} * exp(2 pi i t * {f})'.format(c=coef,
#                                                     f=freq))

# print(len(freqs))
# print(len(np.abs(w)))

# plt.stem(freqs,np.abs(w))
# plt.show()

# print(sr)
# print(x)
# print(len(x))

# dur = int(len(x)/sr)
# print(dur/60)

# time = np.arange(0,len(x),256)

# plt.plot(time,x[::256])
# plt.show()