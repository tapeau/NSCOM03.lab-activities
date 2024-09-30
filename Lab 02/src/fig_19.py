import numpy as np
import matplotlib.pyplot as plt

duration = 0.01
t_analog = np.linspace(0, duration, 1000)
t_sampled = np.linspace(0, duration, 80)

frequencies = [500, 1000, 1500, 2000]
analog_signal = sum(np.sin(2 * np.pi * f * t_analog) for f in frequencies)

sampled_signal = sum(np.sin(2 * np.pi * f * t_sampled) for f in frequencies)

levels = 16
quantized_signal = np.round(sampled_signal * (levels / 2)) / (levels / 2)

fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

axs[0].plot(t_analog, analog_signal, label='Analog Signal', color='blue')
axs[0].set_title("Analog Signal")
axs[0].set_ylabel("Amplitude")
axs[0].grid(True)

axs[1].stem(t_sampled, sampled_signal, label='Sampled Signal', linefmt='orange', basefmt=" ", markerfmt="ro")
axs[1].set_title("Sampled Signal (8000 Hz)")
axs[1].set_ylabel("Amplitude")
axs[1].grid(True)

axs[2].step(t_sampled, quantized_signal, label='Digital Signal', where='mid', color='green')
axs[2].set_title("Digital Signal (Quantized to 16 levels)")
axs[2].set_xlabel("Time")
axs[2].set_ylabel("Amplitude")
axs[2].grid(True)

plt.tight_layout()
plt.show()