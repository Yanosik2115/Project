import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,1,0,1,2,1,0])

w = np.fft.rfft(x)

freqs = np.fft.rfftfreq(len(x))

for coef, freq in zip(w, freqs):
    if coef:
        print('{c:>6} * exp(2 pi i t * {f})'.format(c=coef,
                                                    f=freq))

plt.stem(freqs,np.abs(w))
plt.show()