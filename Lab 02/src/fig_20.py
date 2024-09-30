import numpy as np
import matplotlib.pyplot as plt

bandwidth = 200
nyquist_rate = 2 * bandwidth

frequencies = np.linspace(0, bandwidth, 1000)

plt.figure(figsize=(10, 6))
plt.fill_between(frequencies, 0, 1, color='skyblue', alpha=0.5, label='Signal Bandwidth (0 - 200 kHz)')
plt.axvline(x=nyquist_rate, color='red', linestyle='--', label='Sampling Rate (400 kHz)')

plt.xlabel('Frequency (kHz)')
plt.ylabel('Amplitude')
plt.title('Bandwidth and Minimum Sampling Rate for a Low-pass Signal')
plt.legend()
plt.text(nyquist_rate + 10, 0.5, 'Sampling Rate (2 x 200 kHz)', color='red')
plt.text(100, 0.5, 'Signal Bandwidth (0 - 200 kHz)', color='blue')
plt.grid(True)
plt.show()