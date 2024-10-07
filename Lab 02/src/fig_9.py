import matplotlib.pyplot as plt
import numpy as np

binary_sequence = "101101001"

time_step = 1  # Each bit lasts for 1 time unit
total_time = len(binary_sequence) * time_step

time = np.arange(0, total_time, 0.01)

signal = np.zeros_like(time)

for i, bit in enumerate(binary_sequence):
    if bit == '1':
        signal[i * 100:(i + 1) * 100] = 1  # High level for '1'
    else:
        signal[i * 100:(i + 1) * 100] = -1  # Low level for '0'

plt.figure(figsize=(10, 4))
plt.plot(time, signal, drawstyle='steps-post')
plt.title('Polar NRZ-L Encoding')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.yticks([-1, 1], ['0', '1'])
plt.xlim(0, 9)
plt.ylim(-1, 1.004)
plt.show()