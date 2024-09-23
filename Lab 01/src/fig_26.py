import matplotlib.pyplot as plt

bandwidth_gbps = 1 
distance_km = 12000
light_speed_mps = 2.4e8
message_size_kb = 2.5

bandwidth_bps = bandwidth_gbps * 1e9
message_size_bits = message_size_kb * 8 * 1024

transmission_time_ms = message_size_bits / bandwidth_bps * 1000

distance_m = distance_km * 1000
propagation_time_s = distance_m / light_speed_mps
propagation_time_ms = propagation_time_s * 1000

total_time_ms = transmission_time_ms + propagation_time_ms

labels = ['Transmission Time', 'Propagation Time', 'Total Time']
times_ms = [transmission_time_ms, propagation_time_ms, total_time_ms]

plt.bar(labels, times_ms, color=['blue', 'orange', 'green'])
plt.ylabel('Time (ms)')
plt.title('Transmission and Propagation Time for 2.5 KB Message')
plt.ylim(0, max(times_ms) + 1)

for i, v in enumerate(times_ms):
    plt.text(i, v + 0.1, f"{v:.3f} ms", ha='center')

plt.grid(axis='y')
plt.show()
