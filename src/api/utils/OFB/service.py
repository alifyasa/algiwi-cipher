IV = '0'

def extend_bit_ofb(bit, encryption_length):
  # Panjang bit harus kelipatan panjang enkripsi
  while len(bit) % encryption_length != 0:
    bit += '0'
  return bit

'''
r-bit dari hasil enkripsi antrian disalin menjadi elemen posisi paling kanan di antrian
'''
# Encrypt bit using OFB
def encrypt_ofb(bit, key, encryption_length):
  encrypted_bit = ""
  for i in range(0, len(bit), encryption_length):
    if (i == 0):
      queue = format(int(IV, 2), f'0{len(key)}b')
    encrypted_queue = format(int(queue, 2) ^ int(key, 2), f'0{len(key)}b')
    block = bit[i:i+encryption_length]
    xor_result = int(block, 2) ^ int(encrypted_queue[:encryption_length], 2)
    xor_result = format(xor_result, f'0{encryption_length}b')
    queue = queue[encryption_length:] + encrypted_queue[:encryption_length]
    encrypted_bit += xor_result
  return encrypted_bit

# Decrypt bit using OFB
def decrypt_ofb(bit, key, encryption_length):
  decrypted_bit = ""
  for i in range(0, len(bit), encryption_length):
    if (i == 0):
      queue = format(int(IV, 2), f'0{len(key)}b')
    encrypted_queue = format(int(queue, 2) ^ int(key, 2), f'0{len(key)}b')
    block = bit[i:i+encryption_length]
    xor_result = int(block, 2) ^ int(encrypted_queue[:encryption_length], 2)
    xor_result = format(xor_result, f'0{encryption_length}b')
    queue = queue[encryption_length:] + encrypted_queue[:encryption_length]
    decrypted_bit += xor_result
  return decrypted_bit