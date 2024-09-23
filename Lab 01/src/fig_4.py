import numpy as np
import matplotlib.pyplot as plt

amplitude = 1.0
frequency = 1.0
phase = 0
duration = 2.0

t = np.linspace(0, duration, 1000)  # 1000 points over the duration

sine_wave = amplitude * np.sin(2 * np.pi * frequency * t + phase)


plt.figure(figsize=(10, 5))
plt.plot(t, sine_wave, label='Sine Wave', color='blue')
plt.title('Sine Wave Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.grid()
plt.legend()
plt.xlim(0, duration)
plt.ylim(-amplitude * 1.5, amplitude * 1.5)
plt.show()