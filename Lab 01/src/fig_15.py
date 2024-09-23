import numpy as np
import matplotlib.pyplot as plt

power_ratios = np.linspace(0.01, 1, 100)

attenuation_dB = 10 * np.log10(power_ratios)

plt.figure(figsize=(10, 6))
plt.plot(power_ratios, attenuation_dB, label='Attenuation', color='blue')

specific_ratio = 0.5
specific_attenuation = 10 * np.log10(specific_ratio)
plt.scatter(specific_ratio, specific_attenuation, color='red')
plt.text(specific_ratio, specific_attenuation, f'  {specific_attenuation:.2f} dB', color='red')

plt.title('Signal Attenuation in dB')
plt.xlabel('Power Ratio (P2 / P1)')
plt.ylabel('Attenuation (dB)')
plt.axhline(0, color='black', linewidth=0.5, ls='--')  # Reference line at 0 dB
plt.axvline(1, color='black', linewidth=0.5, ls='--')  # Reference line at P2 = P1
plt.legend()
plt.grid()

plt.show()
