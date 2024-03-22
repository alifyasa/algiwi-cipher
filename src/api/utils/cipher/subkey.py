from feistel import feistel_network

euler_number = [
    2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4, 5, 9, 0, 4, 5, 
    2, 3, 5, 3, 6, 0, 2, 8, 7, 4, 7, 1, 3, 5, 2, 6, 
    6, 2, 4, 9, 7, 7, 5, 7, 2, 4, 7, 0, 9, 3, 6, 9, 
    9, 9, 5, 9, 5, 7, 4, 9, 6, 6, 9, 6, 7, 6, 2, 7, 
    7, 2, 4, 0, 7, 6, 6, 3, 0, 3, 5, 3, 5, 4, 7, 5, 
    9, 4, 5, 7, 1, 3, 8, 2, 1, 7, 8, 5, 2, 5, 1, 6, 
    6, 4, 2, 7, 4, 2, 7, 4, 6, 6, 3, 9, 1, 9, 3, 2, 
    0, 0, 3, 0, 5, 9, 9, 2, 1, 8, 1, 7, 4, 1, 3, 5, 
    9, 6, 6, 2, 9, 0, 4, 3, 5, 7, 2, 9, 0, 0, 3, 3, 
    4, 2, 9, 5, 2, 6, 0, 5, 9, 5, 6, 3, 0, 7, 3, 8, 
    1, 3, 2, 3, 2, 8, 6, 2, 7, 9, 4, 3, 4, 9, 0, 7, 
    6, 3, 2, 3, 3, 8, 2, 9, 8, 8, 0, 7, 5, 3, 1, 9, 
    5, 2, 5, 1, 0, 1, 9, 0, 1, 1, 5, 7, 3, 8, 3, 4, 
    1, 8, 7, 9, 3, 0, 7, 0, 2, 1, 5, 4, 0, 8, 9, 1, 
    4, 9, 9, 3, 4, 8, 8, 4, 1, 6, 7, 5, 0, 9, 2, 4, 
    4, 7, 6, 1, 4, 6, 0, 6, 6, 8, 0, 8, 2, 2, 6, 4
]

def generate_sub_keys(key: int, round_size: int):
    sub_keys = [0] * round_size
    for i in range(round_size):
        sub_keys[i] = feistel_network(key, euler_number[i * 16: (i + 1) * 16])
    return sub_keys

def test():
    key = 26062003
    print(f"Key           : {key:0128b}")
    sub_keys = generate_sub_keys(key, 16)
    for idx, sub_key in enumerate(sub_keys):
        print(f"Sub-Key {idx:>2d}    : {sub_key:0128b}")

if __name__ == "__main__":
    test()