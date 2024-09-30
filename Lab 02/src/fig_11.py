import matplotlib.pyplot as plt

R_values = range(0, 5)

avg_signal_rate = []
min_bandwidth = []

for R in R_values:
    S = 0.5 * R * 1
    avg_signal_rate.append(S)
    Bmin = S
    min_bandwidth.append(Bmin)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(R_values, avg_signal_rate, marker='o')
plt.title('Average Signal Rate vs R (Mbps)')
plt.xlabel('R (Mbps)')
plt.ylabel('Average Signal Rate (kbaud)')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(R_values, min_bandwidth, marker='o', color='orange')
plt.title('Minimum Bandwidth vs R (Mbps)')
plt.xlabel('R (Mbps)')
plt.ylabel('Minimum Bandwidth (kHz)')
plt.grid(True)

plt.tight_layout()
plt.show()