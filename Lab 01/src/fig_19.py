import numpy as np
import matplotlib.pyplot as plt

signal_power_mW = 10
noise_power_uW = 1

signal_power_uW = signal_power_mW * 1000

SNR_dB = 10 * np.log10(signal_power_uW / noise_power_uW)

print(f"SNR (dB): {SNR_dB:.2f}")

powers = [noise_power_uW, signal_power_uW]
labels = ['Noise Power (1 μW)', 'Signal Power (10 mW)']
colors = ['blue', 'orange']

plt.bar(labels, powers, color=colors)
plt.yscale('log')
plt.ylabel('Power (μW)')
plt.title('Signal vs. Noise Power')
plt.axhline(y=noise_power_uW, color='red', linestyle='--', label='Noise Level (1 μW)')
plt.axhline(y=signal_power_uW, color='green', linestyle='--', label='Signal Level (10 mW)')
plt.legend()
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.show()
