import matplotlib.pyplot as plt

data_rates = [1000, 1000000]

clock_speed_diffs = [0, 0.025, 0.050, 0.075, 0.1]

extra_bits_per_second = {1000: [], 1000000: []}

for diff in clock_speed_diffs:
    for rate in data_rates:
        extra_bits = rate * (1 + diff / 100) - rate
        extra_bits_per_second[rate].append(extra_bits)

plt.figure(figsize=(10, 6))

plt.plot(clock_speed_diffs, extra_bits_per_second[1000], marker='o', label='1 kbps')

plt.plot(clock_speed_diffs, extra_bits_per_second[1000000], marker='s', label='1 Mbps')

plt.xlabel('Receiver Clock Speed Difference (%)')
plt.ylabel('Extra Bits per Second')
plt.title('Extra Bits per Second vs Receiver Clock Speed Difference')
plt.legend()
plt.grid(True)
plt.xlim(0, 0.1)
plt.ylim(0, 1000)
plt.show()