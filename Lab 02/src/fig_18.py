import numpy as np
import matplotlib.pyplot as plt

f = 1
T = 1 / f
t = np.linspace(0, 3 * T, 1500)

sine_wave = np.sin(2 * np.pi * f * t)

fs_nyquist = 2 * f
fs_oversample = 4 * f
fs_undersample = f

t_nyquist = np.arange(0.25, 3 * T, 1 / fs_nyquist)
t_oversample = np.arange(0, 3 * T, 1 / fs_oversample)
t_undersample = np.arange(0.25, 3 * T, 0.75 / fs_undersample)

sampled_nyquist = np.sin(2 * np.pi * f * t_nyquist)
sampled_oversample = np.sin(2 * np.pi * f * t_oversample)
sampled_undersample = np.sin(2 * np.pi * f * t_undersample)

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, sine_wave, label='Original Sine Wave', color='black')
plt.plot(t_nyquist, sampled_nyquist, 'ro-', label='Sampled at Nyquist Rate (fs = 2f)')
plt.title('Nyquist Rate Sampling')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, sine_wave, label='Original Sine Wave', color='black')
plt.plot(t_oversample, sampled_oversample, 'go-', label='Sampled at Oversampling Rate (fs = 4f)')
plt.title('Oversampling')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t, sine_wave, label='Original Sine Wave', color='black')
plt.plot(t_undersample, sampled_undersample, 'bo-', label='Sampled at Undersampling Rate (fs = f)')
plt.title('Undersampling')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()