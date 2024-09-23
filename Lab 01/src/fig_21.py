import numpy as np
import matplotlib.pyplot as plt

bandwidth_hz = 3000
signal_to_noise_ratio = 3162

capacity_bps = bandwidth_hz * np.log2(1 + signal_to_noise_ratio)

print(f"Shannon Capacity: {capacity_bps:.2f} bps")

plt.figure(figsize=(8, 5))
plt.bar(['Shannon Capacity'], [capacity_bps], color='skyblue')
plt.ylabel('Capacity (bps)')
plt.title('Shannon Capacity of a Telephone Line')
plt.ylim(0, capacity_bps * 1.2)
plt.grid(axis='y')

plt.show()
