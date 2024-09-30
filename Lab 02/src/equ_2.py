import math

def nyquist_max_data_rate(bandwidth, num_signal_levels):
    """
    Calculate the maximum data rate of a noiseless channel according to the Nyquist theorem.

    Parameters:
    bandwidth (float): The bandwidth of the channel in Hertz (Hz).
    num_signal_levels (int): The number of signal levels used in the communication.

    Returns:
    float: The maximum data rate in bits per second (bps).
    """
    max_data_rate = 2 * bandwidth * math.log2(num_signal_levels)
    
    return max_data_rate
