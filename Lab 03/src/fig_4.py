def xor(a, b):
    """Perform XOR operation on two binary strings."""
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(dividend, divisor):
    """Perform modulo-2 division."""
    pick = len(divisor)
    tmp = dividend[0:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0'*pick, tmp) + dividend[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)

    return tmp

def calculate_crc(data, generator):
    """Calculate the CRC checksum."""
    l_gen = len(generator)
    appended_data = data + '0'*(l_gen-1)
    remainder = mod2div(appended_data, generator)
    return remainder

def main():
    # Prompt the user for input
    data = input("Enter the binary data: ")
    generator = input("Enter the generator polynomial: ")

    # Calculate the CRC checksum
    crc = calculate_crc(data, generator)

    # Display the result
    print(f"The CRC checksum is: {crc}")

if __name__ == "__main__":
    main()
