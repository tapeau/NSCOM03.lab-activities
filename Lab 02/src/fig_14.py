import matplotlib.pyplot as plt
import numpy as np

bit_sequence = "010011"

bit_period = 1

time = []
differential_manchester_signal = []

current_time = 0
previous_state = 1

for bit in bit_sequence:
    if bit == '0':
        time.extend([current_time, current_time + bit_period / 2, current_time + bit_period])
        differential_manchester_signal.extend([-previous_state, previous_state, previous_state])
    else:
        time.extend([current_time, current_time + bit_period / 2, current_time + bit_period])
        differential_manchester_signal.extend([previous_state, -previous_state, -previous_state])
    
    previous_state = differential_manchester_signal[-1]
    current_time += bit_period

plt.figure(figsize=(10, 4))
plt.step(time, differential_manchester_signal, where='post', color='blue')
plt.title('Differential Manchester Line Encoding')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.yticks([-1, 1], ['Low', 'High'])
plt.grid(True)
plt.xlim(0, 6)
plt.ylim(-1.004, 1.004)
plt.show()