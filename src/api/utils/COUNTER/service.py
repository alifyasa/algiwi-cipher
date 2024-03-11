COUNTER = '0'

def extend_bit_counter(bit, key):
  # Panjang bit harus kelipatan panjang key
  while len(bit) % len(key) != 0:
    bit += '0'
  return bit

'''
EK(Ti) = (Ti + K) << 1

• Nilai counter harus berbeda dari setiap blok yang dienkripsi. Pada mulanya, 
untuk enkripsi blok pertama, counter diinisialisasi dengan sebuah nilai. 
• Selanjutnya, untuk enkripsi blok-blok berikutnya counter dinaikkan
 (increment) nilainya satu (counter = counter + 1). 
'''
# Encrypt bit using Counter
def encrypt_counter(bit, key):
  encrypted_bit = ""
  for i in range(0, len(bit), len(key)):
    if (i == 0):
      counter = format(int(COUNTER, 2), f'0{len(key)}b')
    encrypted_counter = format(int(counter, 2) ^ int(key, 2), f'0{len(key)}b')
    encrypted_counter = encrypted_counter[1:] + encrypted_counter[0]
    block = bit[i:i+len(key)]
    xor_result = int(block, 2) ^ int(encrypted_counter, 2)
    xor_result = format(xor_result, f'0{len(key)}b')
    counter = format(int(counter, 2) + 1, f'0{len(key)}b')
    encrypted_bit += xor_result
  return encrypted_bit

# Decrypt bit using Counter
def decrypt_counter(bit, key):
  decrypted_bit = ""
  for i in range(0, len(bit), len(key)):
    if (i == 0):
      counter = format(int(COUNTER, 2), f'0{len(key)}b')
    encrypted_counter = format(int(counter, 2) ^ int(key, 2), f'0{len(key)}b')
    encrypted_counter = encrypted_counter[1:] + encrypted_counter[0]
    block = bit[i:i+len(key)]
    xor_result = int(block, 2) ^ int(encrypted_counter, 2)
    xor_result = format(xor_result, f'0{len(key)}b')
    counter = format(int(counter, 2) + 1, f'0{len(key)}b')
    decrypted_bit += xor_result
  return decrypted_bit