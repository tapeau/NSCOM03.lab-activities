import matplotlib.pyplot as plt

frequencies = range(0, 4001, 100)

sampling_rates = []
bit_rates = []

bits_per_sample = 8

for freq in frequencies:
    sampling_rate = 2 * freq
    bit_rate = sampling_rate * bits_per_sample
    
    sampling_rates.append(sampling_rate)
    bit_rates.append(bit_rate)

plt.figure(figsize=(10, 6))
plt.plot(frequencies, sampling_rates, label='Sampling Rate (samples/s)', marker='o')
plt.plot(frequencies, bit_rates, label='Bit Rate (bps)', marker='s')

plt.xlabel('Frequency')
plt.ylabel('Rate')
plt.title('Sampling Rate and Bit Rate for Human Voice')
plt.legend()
plt.grid(True)
plt.xlim(0, 4000)
plt.ylim(0, 64000)
plt.show()