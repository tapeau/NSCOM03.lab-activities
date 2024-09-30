import matplotlib.pyplot as plt
import numpy as np

bit_sequence = "01001"

T = 1

time = np.arange(0, len(bit_sequence) * T, 0.01)

signal = np.zeros_like(time)

for i, bit in enumerate(bit_sequence):
    start = i * T
    end = (i + 1) * T
    if bit == '1':
        signal[(time >= start) & (time < end)] = 1
        signal[(time >= start + T/2) & (time < end)] = 0
    elif bit == '0':
        signal[(time >= start) & (time < end)] = -1
        signal[(time >= start + T/2) & (time < end)] = 0

plt.figure(figsize=(10, 4))
plt.plot(time, signal, drawstyle='steps-post')

plt.axhline(0, color='red', linestyle='--')

plt.title('Polar RZ Encoding')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.ylim(-1.5, 1.5)
plt.show()