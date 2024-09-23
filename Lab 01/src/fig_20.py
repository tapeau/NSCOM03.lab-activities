import numpy as np
import matplotlib.pyplot as plt

bandwidth = 3000
signal_levels = 2

bit_rate = 2 * bandwidth * np.log2(signal_levels)

plt.figure(figsize=(8, 5))
plt.bar(['Nyquist Bit Rate'], [bit_rate], color='blue')
plt.ylim(0, bit_rate * 1.2)
plt.ylabel('Bit Rate (bps)')
plt.title('Nyquist Bit Rate Calculation')
plt.text(0, bit_rate + 100, f'{bit_rate:.0f} bps', ha='center', va='bottom', fontsize=12)

plt.grid(axis='y')
plt.show()
