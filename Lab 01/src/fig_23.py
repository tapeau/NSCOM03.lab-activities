import numpy as np
import matplotlib.pyplot as plt

propagation_time = 10
transmission_time = 5
queuing_time = 2
processing_delay = 3

num_packets = np.arange(1, 101)

latency = (propagation_time +
           transmission_time +
           queuing_time * num_packets +
           processing_delay)

plt.figure(figsize=(10, 6))
plt.plot(num_packets, latency, label='Latency', color='blue', marker='o')
plt.title('Latency vs Number of Packets')
plt.xlabel('Number of Packets')
plt.ylabel('Latency (ms)')
plt.grid()
plt.legend()
plt.show()
