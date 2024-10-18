import numpy as np
import matplotlib.pyplot as plt

# Data to be transmitted (example sequence)
data = [1, 0, 1, 1, 0, 0, 1, 1]

phase = 0
phases = [phase]

for bit in data:
    if bit == 1:
        phase = (phase + np.pi) % (2 * np.pi)
    phases.append(phase)

bit_duration = 1
time = np.arange(0, len(data) + 1, 0.01)

signal = np.zeros_like(time)
for i in range(len(data)):
    t_index = (time >= i) & (time < i + 1)
    signal[t_index] = np.cos(phases[i])

# Plotting
plt.figure(figsize=(10, 4))
plt.plot(time, signal, label='PSK with NRZ-I', color='b')
plt.step(np.arange(len(data) + 1), np.cos(phases), where='post', linestyle='--', color='r', alpha=0.5, label='Phase changes')

plt.title('PSK with NRZ-I Linecoding')
plt.xlabel('Time (units)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.xlim(0, 9)
plt.ylim(-1.01, 1.01)
plt.show()
