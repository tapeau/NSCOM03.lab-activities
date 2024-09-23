import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

t = np.linspace(0, 10, 1000)

signal = np.cumsum(np.random.randn(len(t)))

plt.figure(figsize=(12, 6))
plt.plot(t, signal, label='Random Nonperiodic Signal', color='blue')
plt.title('Random Nonperiodic Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()
plt.show()
