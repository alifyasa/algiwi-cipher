IV = '0'

def extend_bit_cfb(bit, encryption_length):
  # Panjang bit harus kelipatan panjang enkripsi
  while len(bit) % encryption_length != 0:
    bit += '0'
  return bit

'''
Steps of operation are:

1. Firstly, Load the IV in the top register.
2. Then, Encrypt the data value in the top register with the underlying block cipher with key K to the block.
3. Then, take only 's' number of most significant bits as left bits of the output of the encryption process and XOR them with 's' bit plaintext or original text message block to generate ciphertext block in cryptography.
4. This, Feed ciphertext block into the top register by shifting already present data to the left and continue the operation till all plaintext or original text blocks are processed in this mode.
5. Essentially, the previous ciphertext block is encrypted with the key, and then the result is XORed to the current plaintext block or original text.
6. Similar steps are followed for decryption cryptography. Pre-decided IV is initially loaded at the start of decryption in the cryptography.
'''
# Encrypt bit using CFB
def encrypt_cfb(bit, key, encryption_length):
  encrypted_bit = ""
  for i in range(0, len(bit), encryption_length):
    if (i == 0):
      X = format(int(IV, 2), f'0{len(key)}b')
    encrypted_key = format(int(X, 2) ^ int(key, 2), f'0{len(key)}b')
    block = bit[i:i+encryption_length]
    xor_result = int(block, 2) ^ int(encrypted_key[:encryption_length], 2)
    xor_result = format(xor_result, f'0{encryption_length}b')
    X = X[encryption_length:] + xor_result
    encrypted_bit += xor_result
  return encrypted_bit

# Decrypt bit using CFB
def decrypt_cfb(bit, key, encryption_length):
  decrypted_bit = ""
  for i in range(0, len(bit), encryption_length):
    if (i == 0):
      X = format(int(IV, 2), f'0{len(key)}b')
    encrypted_key = format(int(X, 2) ^ int(key, 2), f'0{len(key)}b')
    block = bit[i:i+encryption_length]
    xor_result = int(block, 2) ^ int(encrypted_key[:encryption_length], 2)
    xor_result = format(xor_result, f'0{encryption_length}b')
    X = X[encryption_length:] + block
    decrypted_bit += xor_result
  return decrypted_bit