import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 1000)
amplitude_modulation = 5 * np.cos(t)

noise1 = 2.5 * np.sin(2 * t)
noise2 = 2.5 * np.cos(2 * t)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, amplitude_modulation, label='ASK (Cosine, Amplitude=5)', linewidth=2)
plt.plot(t, noise1, label='Noise 1 (Sin, Amplitude=2.5)', linestyle='--')
plt.plot(t, noise2, label='Noise 2 (Cos, Amplitude=2.5)', linestyle='--')

plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.title('Amplitude Modulation / ASK with Noise')
plt.legend()
plt.grid(True)
plt.xlim(0, 6.2)
plt.ylim(-5,5)
plt.show()
