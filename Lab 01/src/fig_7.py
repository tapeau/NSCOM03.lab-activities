import numpy as np
import matplotlib.pyplot as plt

fs = 1000
t = np.arange(0, 1, 1/fs)

frequency1 = 5
frequency2 = 10
frequency3 = 20

sine_wave1 = np.sin(2 * np.pi * frequency1 * t)
sine_wave2 = np.sin(2 * np.pi * frequency2 * t)
square_wave = 0.5 * np.sign(np.sin(2 * np.pi * frequency3 * t))

composite_signal = sine_wave1 + sine_wave2 + square_wave

plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(t, sine_wave1, label='Sine Wave (5 Hz)')
plt.title('Sine Wave (5 Hz)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, sine_wave2, label='Sine Wave (10 Hz)', color='orange')
plt.title('Sine Wave (10 Hz)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t, square_wave, label='Square Wave (20 Hz)', color='green')
plt.title('Square Wave (20 Hz)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

plt.figure(figsize=(12, 4))
plt.plot(t, composite_signal, label='Composite Signal', color='purple')
plt.title('Composite Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
