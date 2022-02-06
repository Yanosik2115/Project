from black import TRANSFORMED_MAGICS
import pydub 
import numpy as np
import matplotlib.pyplot as plt

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

print(sr)
print(x)
print(len(x))

time = np.arange(0,len(x),256)

plt.plot(time,x[::256])
plt.show()