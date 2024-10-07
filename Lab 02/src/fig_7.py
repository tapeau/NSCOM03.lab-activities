import numpy as np
import matplotlib.pyplot as plt

bit_sequence = [1, 0, 1, 1, 0, 0, 1, 0]

bit_period = 1

time = np.arange(0, len(bit_sequence) * bit_period, 0.01)

signal = np.zeros_like(time)

for i, bit in enumerate(bit_sequence):
    if bit == 1:
        signal[int(i * bit_period / 0.01):int((i + 1) * bit_period / 0.01)] = 1

plt.figure(figsize=(10, 4))
plt.plot(time, signal, drawstyle='steps-pre')
plt.title('Unipolar NRZ Scheme')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.yticks([0, 1])
plt.grid(True)
plt.xlim(0, 8)
plt.ylim(0, 1.004)
plt.show()