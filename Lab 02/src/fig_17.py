import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)
analog_signal = np.sin(2 * np.pi * 5 * t) 

sampling_rate = 50
sampling_interval = int(1000 / sampling_rate)
t_samples = t[::sampling_interval]
analog_samples = analog_signal[::sampling_interval]

ideal_samples = np.zeros_like(t)
ideal_samples[::sampling_interval] = analog_samples

plt.figure(figsize=(12, 6))

plt.plot(t, analog_signal, label="Analog Signal", color="blue", linewidth=2)
plt.step(t, ideal_samples, where='post', label="Ideal Sampling", color="red", linestyle="--")
plt.scatter(t_samples, analog_samples, color='black', zorder=5, marker="o", label="Sample Points")

plt.title("PCM Ideal Sampling", fontsize=16)
plt.xlabel("Time", fontsize=12)
plt.ylabel("Amplitude", fontsize=12)
plt.legend(loc="upper right", fontsize=10)
plt.grid(True)

plt.tight_layout()
plt.show()