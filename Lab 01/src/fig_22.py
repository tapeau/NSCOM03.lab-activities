import numpy as np
import matplotlib.pyplot as plt

bandwidth = 1e6
snr = 63
C = bandwidth * np.log2(1 + snr)

nyquist_bit_rate = 2 * bandwidth

print(f"Shannon Capacity (C): {C / 1e6:.2f} Mbps")
print(f"Nyquist Bit Rate: {nyquist_bit_rate / 1e6:.2f} Mbps")

plt.figure(figsize=(10, 6))
plt.bar(['Shannon Capacity', 'Nyquist Bit Rate'], [C / 1e6, nyquist_bit_rate / 1e6], color=['blue', 'orange'])
plt.title('Shannon Capacity vs. Nyquist Bit Rate')
plt.ylabel('Bit Rate (Mbps)')
plt.ylim(0, max(C, nyquist_bit_rate) / 1e6 + 1)
plt.grid(axis='y')

plt.show()
