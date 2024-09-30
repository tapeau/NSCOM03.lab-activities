def calculate_S(c, R, N=1000):
    """
    Calculate the value of S based on the given equation:
    S = c * N * R
    
    Parameters:
    c (float): The coefficient.
    R (float): The rate.
    N (int): The number of symbols (default is 1000).
    
    Returns:
    float: The value of S.
    """
    S = c * N * R
    return S

c = 0.5
R = 1
S = calculate_S(c, R)