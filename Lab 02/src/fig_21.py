import matplotlib.pyplot as plt

min_voltage = -20
max_voltage = 20
num_levels = 8

zone_width = (max_voltage - min_voltage) / num_levels
zone_boundaries = [min_voltage + i * zone_width for i in range(num_levels + 1)]
midpoints = [min_voltage + (i + 0.5) * zone_width for i in range(num_levels)]
fig, ax = plt.subplots(figsize=(10, 6))

for i in range(num_levels):
    ax.axvspan(zone_boundaries[i], zone_boundaries[i+1], alpha=0.3, color='blue')

ax.scatter(midpoints, [0]*num_levels, color='red', zorder=5)

for midpoint in midpoints:
    ax.annotate(f'{midpoint}V', (midpoint, 0.1), textcoords="offset points", xytext=(0,10), ha='center')

ax.set_xlim(min_voltage, max_voltage)
ax.set_xticks(zone_boundaries)
ax.set_xlabel('Voltage (V)')
ax.set_yticks([])
ax.set_title('Quantization Zones and Midpoints')
plt.grid(True)
plt.show()