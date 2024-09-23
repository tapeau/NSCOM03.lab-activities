import numpy as np
import matplotlib.pyplot as plt

message_sizes_kb = np.linspace(1, 10240, 100)
bandwidths_mbps = [1, 10, 20, 50, 100]

message_sizes_bytes = message_sizes_kb * 1024

plt.figure(figsize=(10, 6))

for bandwidth in bandwidths_mbps:
    bandwidth_bps = bandwidth * 1_000_000 / 8
    transmission_time = message_sizes_bytes / bandwidth_bps
    plt.plot(message_sizes_kb, transmission_time, label=f'{bandwidth} Mbps')

plt.title('Transmission Time vs. Message Size')
plt.xlabel('Message Size (KB)')
plt.ylabel('Transmission Time (seconds)')
plt.yscale('log')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.tight_layout()

plt.show()
