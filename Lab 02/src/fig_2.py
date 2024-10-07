import matplotlib.pyplot as plt
import numpy as np

binary_sequence = "101101"

time_step = 1
bit_duration = 1

time = np.arange(0, len(binary_sequence) * bit_duration, time_step)

unipolar_signal = []
for bit in binary_sequence:
    if bit == '1':
        unipolar_signal.extend([1] * bit_duration)
    else:
        unipolar_signal.extend([0] * bit_duration)

plt.figure(figsize=(10, 4))
plt.step(time, unipolar_signal, where='post', color='blue', linewidth=2)
plt.title('Unipolar Line Coding')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.yticks([0, 1], ['0', '1'])
plt.xlim(0, 5)
plt.ylim(0, 1)
plt.show()