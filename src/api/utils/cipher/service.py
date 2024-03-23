from utils.cipher.subkey import generate_sub_keys
from utils.cipher.feistel import feistel_network
# from subkey import generate_sub_keys
# from feistel import feistel_network

def encrypt_block(block_plaintext: int, key: int) -> int:
    data_len = len(f"{block_plaintext:08b}")
    assert data_len <= 128, f"Input size {data_len}, expected less than 128"
    sub_keys = generate_sub_keys(key, 16)
    ciphertext = feistel_network(block_plaintext, sub_keys)
    return ciphertext

def decrypt_block(block_ciphertext:int, key: int) -> int:
    data_len = len(f"{block_ciphertext:08b}")
    assert data_len <= 128, f"Input size {data_len}, expected less than 128"
    sub_keys = generate_sub_keys(key, 16)
    plaintext = feistel_network(block_ciphertext, sub_keys, decrypt=True)
    return plaintext

def test():
    plaintext = 20030626
    key = "alifyasa"

    formatted_key = int(''.join(format(ord(char), '08b') for char in key), 2)
    print(f"Plaintext : {plaintext:0128b}")
    print(f"Key       : {formatted_key:0128b}")

    ciphertext = encrypt_block(plaintext, formatted_key)
    print(f"Ciphertext: {ciphertext:0128b}")

    decrypted_ciphertext = decrypt_block(ciphertext, formatted_key)
    print(f"Decrypted : {decrypted_ciphertext:0128b}")

if __name__ == "__main__":
    test()