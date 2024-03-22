P_BOX = [
    43, 49,  6, 24, 45, 32, 42, 44,
    28, 13, 62, 37, 57, 23, 50, 56,
    33,  8,  5, 51, 55, 54, 36, 58,
    61, 53, 40, 60, 34,  2, 15,  0,
     4, 29, 12, 46, 21,  7, 22, 26,
     9, 47, 19,  1,  3, 52, 59, 63,
    17, 20, 18, 31, 27, 35, 11, 38,
    25, 16, 48, 39, 30, 41, 10, 14,
]

INV_P_BOX = [
    31, 43, 29, 44, 32, 18,  2, 37,
    17, 40, 62, 54, 34,  9, 63, 30,
    57, 48, 50, 42, 49, 36, 38, 13,
     3, 56, 39, 52,  8, 33, 60, 51,
     5, 16, 28, 53, 22, 11, 55, 59,
    26, 61,  6,  0,  7,  4, 35, 41,
    58,  1, 14, 19, 45, 25, 21, 20,
    15, 12, 23, 46, 27, 24, 10, 47,
]

def permutate(input_int: int) -> int:
    """
    Permutate half-byte
    """
    output_int = 0  # Initialize the output integer
    for input_pos, output_pos in enumerate(P_BOX):
        # Extract the bit at the current input position
        input_bit = (input_int >> input_pos) & 1
        # Set the extracted bit at the corresponding output position
        output_int |= (input_bit << output_pos)
    
    return output_int

def inv_permutate(input_int: int) -> int :
    """
    Inverse permutate half-byte
    """
    output_int = 0  # Initialize the output integer
    for input_pos, output_pos in enumerate(INV_P_BOX):
        # Extract the bit at the current input position
        input_bit = (input_int >> input_pos) & 1
        # Set the extracted bit at the corresponding output position
        output_int |= (input_bit << output_pos)
    
    return output_int

def test():
    print("===== PERMUTATION TEST =====")
    input_int = 260603
    print(f"Original  : {input_int:064b}")
    permutated_int = permutate(input_int)
    print(f"Permutated: {permutated_int:064b}")
    original_int = inv_permutate(permutated_int)
    print(f"Original  : {original_int:064b}")

if __name__ == "__main__":
    test()