def get_binary_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = input(f"Enter binary string for row {i+1} (length {cols}): ")
        if len(row) != cols or not all(bit in '01' for bit in row):
            raise ValueError("Invalid input. Please enter a binary string of the correct length.")
        matrix.append(row)
    return matrix

def calculate_row_parity(matrix):
    row_parity = []
    for row in matrix:
        parity_bit = '0' if row.count('1') % 2 == 0 else '1'
        row_parity.append(parity_bit)
    return row_parity

def calculate_column_parity(matrix):
    cols = len(matrix[0])
    col_parity = []
    for col in range(cols):
        col_bits = [matrix[row][col] for row in range(len(matrix))]
        parity_bit = '0' if col_bits.count('1') % 2 == 0 else '1'
        col_parity.append(parity_bit)
    return col_parity

def main():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    matrix = get_binary_matrix(rows, cols)
    
    print("\nOriginal Matrix:")
    for row in matrix:
        print(row)
    
    row_parity = calculate_row_parity(matrix)
    print("\nRow Parity Bits:")
    print(" ".join(row_parity))
    
    col_parity = calculate_column_parity(matrix)
    print("\nColumn Parity Bits:")
    print(" ".join(col_parity))
    
    # Add row parity to the matrix
    matrix.append("".join(row_parity))
    
    # Add column parity to the matrix
    for i in range(rows + 1):
        if i < rows:
            matrix[i] += col_parity[i]
        else:
            matrix[i] += '0'  # Last row (parity row) has no column parity bit
    
    print("\nMatrix with Parity Bits:")
    for row in matrix:
        print(row)

if __name__ == "__main__":
    main()
