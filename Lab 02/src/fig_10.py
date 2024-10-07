import matplotlib.pyplot as plt
import numpy as np

bit_sequence = '101101001'

time_step = 1
total_time = len(bit_sequence) * time_step

time = np.arange(0, total_time, time_step)

signal = np.zeros(len(time))

previous_state = -1  # -1 represents low, 1 represents high

for i, bit in enumerate(bit_sequence):
    if bit == '1':
        # Invert the signal if the bit is '1'
        previous_state = -previous_state
    signal[i] = previous_state

plt.figure(figsize=(10, 4))
plt.step(time, signal, where='post', color='blue', linewidth=2)
plt.title('Polar NRZ-I Encoding')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.yticks([-1, 1], ['Low', 'High'])
plt.grid(True)
plt.xlim(0, 8.01)
plt.ylim(-1, 1)
plt.show()