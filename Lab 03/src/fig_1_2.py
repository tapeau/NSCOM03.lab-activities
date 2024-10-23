def one_dimensional_parity_check(binary_string, parity_type):
    # Count the number of '1's in the binary string
    count_ones = binary_string.count('1')
    
    # Determine the expected parity
    if parity_type == "even":
        expected_parity = count_ones % 2 == 0
    elif parity_type == "odd":
        expected_parity = count_ones % 2 != 0
    else:
        return "Invalid parity type. Please enter 'odd' or 'even'."
    
    # Return the result based on the expected parity
    if expected_parity:
        return "Parity check passed."
    else:
        return "Parity check failed."

# Inputs
binary_string = input("Enter the binary string: ")
parity_type = input("Enter the parity type ('odd' or 'even'): ")

# Perform the parity check
result = one_dimensional_parity_check(binary_string, parity_type)
print(result)
