def crc32(data, polynomial):
    """Calculate the CRC-32 checksum."""
    # Initialize the CRC register
    crc = 0xFFFFFFFF

    # Process each byte in the data
    for byte in data:
        crc ^= ord(byte)
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ polynomial
            else:
                crc >>= 1

    # Return the final CRC value
    return crc ^ 0xFFFFFFFF

def main():
    # Prompt the user for input
    data = input("Enter the binary data: ")
    generator_hex = input("Enter the 32-bit generator polynomial in hexadecimal format (e.g., 0xEDB88320): ")

    # Convert the generator polynomial from hexadecimal to integer
    generator = int(generator_hex, 16)

    # Calculate the CRC-32 checksum
    crc = crc32(data, generator)

    # Display the result
    print(f"The CRC-32 checksum is: {crc:08X}")

if __name__ == "__main__":
    main()
