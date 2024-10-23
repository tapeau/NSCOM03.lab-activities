def calculate_checksum(numbers):
    # Initialize the checksum to 0
    checksum = 0
    
    # Sum all the numbers in the array
    for number in numbers:
        checksum += number
    
    # Return the checksum
    return checksum % 10

def main():
    # Prompt the user to enter the array of decimal numbers
    input_numbers = input("Enter a list of decimal numbers separated by spaces: ")
    
    # Convert the input string into a list of integers
    numbers = list(map(int, input_numbers.split()))
    
    # Calculate the checksum
    checksum = calculate_checksum(numbers)
    
    # Print the result
    print(f"The checksum of the array is: {checksum}")

if __name__ == "__main__":
    main()
