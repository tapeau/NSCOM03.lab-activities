def calculate_quantization_step(max_amplitude, min_amplitude, num_levels):
    """
    Calculate the quantization step size (Δ) based on the maximum and minimum amplitude values
    and the number of quantization levels (L).

    Parameters:
    max_amplitude (float): The maximum amplitude value.
    min_amplitude (float): The minimum amplitude value.
    num_levels (int): The number of quantization levels (L).

    Returns:
    float: The quantization step size (Δ).
    """
    
    delta = (max_amplitude - min_amplitude) / (num_levels)
    return delta

result = calculate_quantization_step(20, -20, 8)
print(result)