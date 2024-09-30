def calculate_sampling_rate(base_rate, multiplier):
    """
    Calculate the sampling rate based on the given base rate and multiplier.

    Parameters:
    base_rate (int): The base sampling rate.
    multiplier (int): The multiplier to apply to the base rate.

    Returns:
    int: The calculated sampling rate.
    """
    return base_rate * multiplier

base_rate = 4000
multiplier = 2
calculated_sampling_rate = calculate_sampling_rate(base_rate, multiplier)

print(calculated_sampling_rate)