import numpy as np
import matplotlib.pyplot as plt

# Parameters
sampling_rate = 1000
t = np.linspace(0, 1, sampling_rate, endpoint=False)

carrier_freq = 5
carrier_amplitude = 7
carrier = carrier_amplitude * np.sin(2 * np.pi * carrier_freq * t)

modulating_signal = np.random.choice([0, 1], size=len(t))
modulated_signal = carrier * modulating_signal

distorted_carrier_before = carrier_amplitude * np.sin(2 * np.pi * carrier_freq * t + np.deg2rad(37))
distorted_modulated_signal = carrier_amplitude * np.sin(2 * np.pi * carrier_freq * t + np.deg2rad(37)) * modulating_signal

# Plotting
plt.figure(figsize=(12, 8))

plt.subplot(4, 1, 1)
plt.plot(t, carrier)
plt.title('Original Carrier Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.xlim(0, 1)
plt.ylim(-7.2, 7.2)

plt.subplot(4, 1, 2)
plt.plot(t, distorted_carrier_before)
plt.title('Distorted Carrier Signal (Before Modulation)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.xlim(0, 1)
plt.ylim(-7.2, 7.2)

plt.subplot(4, 1, 3)
plt.plot(t, modulated_signal)
plt.title('Modulated Signal (Amplitude Shift Keying)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.xlim(0, 1)
plt.ylim(-7.2, 7.2)

plt.subplot(4, 1, 4)
plt.plot(t, distorted_modulated_signal)
plt.title('Distorted Modulated Signal (After Modulation)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.xlim(0, 1)
plt.ylim(-7.2, 7.2)

plt.tight_layout()
plt.show()
