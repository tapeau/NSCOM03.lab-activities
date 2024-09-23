import numpy as np
import matplotlib.pyplot as plt

distance = np.linspace(0, 1000, 100)
speed = 300_000_000

propagation_time = distance / speed

plt.figure(figsize=(10, 6))
plt.plot(distance, propagation_time, label='Propagation Time', color='blue')
plt.title('Propagation Time vs. Distance')
plt.xlabel('Distance (meters)')
plt.ylabel('Propagation Time (seconds)')
plt.grid(True)
plt.legend()
plt.show()
