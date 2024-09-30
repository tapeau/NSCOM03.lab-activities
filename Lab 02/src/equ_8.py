def calculate_bit_rate(sample_rate, bits_per_sample):
    """
    Calculate the bit rate using the formula:
    Bit Rate = Sample Rate * Bits per Sample
    
    :param sample_rate: The sample rate in Hz (e.g., 8000 for 8 kHz)
    :param bits_per_sample: The number of bits per sample (e.g., 8 bits)
    :return: The bit rate in bps (bits per second)
    """
    bit_rate = sample_rate * bits_per_sample
    return bit_rate

sample_rate = 8000
bits_per_sample = 8
bit_rate = calculate_bit_rate(sample_rate, bits_per_sample)

print(f"Bit Rate: {bit_rate} bps")
print(f"Bit Rate: {bit_rate / 1000} kbps")