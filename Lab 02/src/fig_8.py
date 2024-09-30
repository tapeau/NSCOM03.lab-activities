import matplotlib.pyplot as plt
import numpy as np

# Example binary data
binary_data = [1, 0, 1, 1, 0, 0, 1, 0]

V_high = 1
V_low = -1

time = np.arange(0, len(binary_data), 0.01)

signal = []
for bit in binary_data:
    if bit == 1:
        signal.extend([V_high] * 100)
    else:
        signal.extend([V_low] * 100)

plt.figure(figsize=(10, 4))
plt.plot(time, signal, label='Polar NRZ Signal')

plt.axhline(y=V_high, color='g', linestyle='--', label='+V (Binary 1)')
plt.axhline(y=V_low, color='r', linestyle='--', label='-V (Binary 0)')

plt.title('Polar Non-Return-to-Zero (NRZ) Line Coding Scheme')
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.legend()

plt.grid(True)
plt.show()