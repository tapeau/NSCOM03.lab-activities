import numpy as np
import matplotlib.pyplot as plt

sampling_rate = 1000
duration = 1
frequency = 5

t = np.arange(0, duration, 1/sampling_rate)

signal = np.sign(np.sin(2 * np.pi * frequency * t))

plt.figure(figsize=(10, 4))
plt.step(t, signal, where='post', label='Digital Signal (Square Wave)', color='blue')
plt.title('Digital Signal - Square Wave')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.ylim(-1.5, 1.5)
plt.grid()
plt.legend()
plt.show()
