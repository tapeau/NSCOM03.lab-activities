def calculate_baud_rate(c, N, r):
    """
    Calculate the baud rate using the formula: S = c * N * (1 / r) bauds

    Parameters:
    c (float): A constant factor.
    N (int): The number of bits per symbol.
    r (float): The symbol rate in symbols per second.

    Returns:
    float: The calculated baud rate in bauds.
    """
    S = c * N * (1 / r)
    return S
