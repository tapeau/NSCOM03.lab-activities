import numpy as np
import matplotlib.pyplot as plt

frequency = 5
sampling_rate = 100
duration = 1

t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

analog_signal = np.sin(2 * np.pi * frequency * t)

plt.figure(figsize=(10, 4))
plt.plot(t, analog_signal, label='Analog Signal (Sine Wave)', color='blue')
plt.title('Analog Signal Representation')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()
