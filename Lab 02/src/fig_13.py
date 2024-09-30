import matplotlib.pyplot as plt
import numpy as np

bit_sequence = "010011"

bit_period = 1

time = []
manchester_signal = []

current_time = 0
for bit in bit_sequence:
    if bit == '0':
        time.extend([current_time, current_time + bit_period / 2, current_time + bit_period])
        manchester_signal.extend([1, -1, -1])
    else:
        time.extend([current_time, current_time + bit_period / 2, current_time + bit_period])
        manchester_signal.extend([-1, 1, 1])
    current_time += bit_period

plt.figure(figsize=(10, 4))
plt.step(time, manchester_signal, where='post', color='blue')
plt.title('Manchester Line Encoding')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.yticks([-1, 1], ['Low', 'High'])
plt.grid(True)
plt.show()