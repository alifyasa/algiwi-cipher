def extend_bit_cbc(bit, key):
  # Panjang bit harus kelipatan panjang key
  while len(bit) % len(key) != 0:
    bit += '0'
  return bit

'''
Encrypt:
1. XOR-kan blok plainteks Pi dengan K dan dengan hasil XOR sebelumnya
2. geser secara wrapping bit-bit dari hasil langkah 1 satu posisi ke kiri
'''
# Encrypt bit using CBC
def encrypt_cbc(bit, key):
  encrypted_bit = ""
  for i in range(0, len(bit), len(key)):
    # XOR-kan blok plainteks Pi dengan K
    block = bit[i:i+len(key)]
    if i == 0:
      xor_result = int(block, 2)
    else:
      xor_result = int(block, 2) ^ int(encrypted_bit[i-len(key):i], 2)
    xor_result = xor_result ^ int(key, 2)
    xor_result = format(xor_result, f'0{len(key)}b')
    # geser secara wrapping bit-bit dari hasil langkah 1 satu posisi ke kiri
    shift_result = xor_result[1:] + xor_result[0]
    encrypted_bit += shift_result
  return encrypted_bit

'''
Decrypt:
1. geser secara wrapping bit-bit dari hasil langkah 1 satu posisi ke kanan
2. XOR-kan blok cipher Ci dengan K dan dengan hasil XOR sebelumnya
'''
# Decrypt bit using CBC
def decrypt_cbc(bit, key):
  decrypted_bit = ""
  for i in range(0, len(bit), len(key)):
    # geser secara wrapping bit-bit dari hasil langkah 1 satu posisi ke kanan
    block = bit[i:i+len(key)]
    shift_result = block[-1] + block[:-1]
    # XOR-kan blok cipher Ci dengan K
    xor_result = int(shift_result, 2) ^ int(key, 2)
    if i == 0:
      xor_result = xor_result
    else:
      xor_result = xor_result ^ int(bit[i-len(key):i], 2)
    xor_result = format(xor_result, f'0{len(key)}b')
    decrypted_bit += xor_result
  return decrypted_bit