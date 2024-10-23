def calculate_checksum(ascii_values):
    # Initialize the checksum to 0
    checksum = 0
    
    # Sum all the ASCII values in the array
    for value in ascii_values:
        checksum += value
    
    # Return the checksum modulo 10
    return checksum % 10

def main():
    # Prompt the user to enter an alphanumeric string
    input_string = input("Enter an alphanumeric string: ")
    
    # Convert the string into a list of ASCII values
    ascii_values = [ord(char) for char in input_string]
    
    # Calculate the checksum
    checksum = calculate_checksum(ascii_values)
    
    # Print the result
    print(f"The checksum of the ASCII values for the string '{input_string}' is: {checksum}")

if __name__ == "__main__":
    main()
