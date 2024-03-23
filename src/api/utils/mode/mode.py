from utils.constant import *
from datetime import datetime
from utils.cipher.service import *

class Mode():
    def __init__(self, bit, key, mode_method, encryption_length=0):
        self.bit = bit
        self.key = key
        self.encryption_length = encryption_length
        self.mode_method = mode_method
        self.start_time = datetime.now()
        self.end_time = datetime.now()
    
    def set_bit(self, bit):
        self.bit = bit

    def set_key(self,key):
        self.key = key

    def set_mode_method(self,mode_method):
        self.mode_method = mode_method

    def set_encryption_length(self,encryption_length):
        self.encryption_length = encryption_length

    def extend_bit_by_key(self):
        # Panjang bit harus kelipatan panjang key
        while len(self.bit) % len(self.key) != 0:
            self.bit += '0'

    def extend_bit_by_encryption_length(self):
        # Panjang bit harus kelipatan panjang enkripsi
        while len(self.bit) % self.encryption_length != 0:
            self.bit += '0'

    # Encrypt bit using CBC
    def encrypt_cbc(self):
        '''
        EK(P) = (P + K) << 1

        Encrypt:
        1. XOR-kan blok plainteks Pi dengan K dan dengan hasil XOR sebelumnya
        2. geser secara wrapping bit-bit dari hasil langkah 1 satu posisi ke kiri
        '''
        encrypted_bit = ""
        # # Calculate the number of zeros to add

        # # Add zeros to the beginning of the string
        if(len(self.key)<128):
           self.key = self.key.zfill(128)

        for i in range(0, len(self.bit), len(self.key)):
            # XOR-kan blok plainteks Pi dengan K dan dengan hasil XOR sebelumnya
            block = self.bit[i:i+len(self.key)]
            if i == 0:
                xor_result = int(block, 2) ^ int(IV, 2)
            else:
                xor_result = int(block, 2) ^ int(encrypted_bit[i-len(self.key):i], 2)

            xor_result = encrypt_block(xor_result, int(self.key,2))

            xor_result = format(xor_result, f'0{len(self.key)}b')

            # geser secara wrapping bit-bit dari hasil langkah 1 satu posisi ke kiri
            shift_result = xor_result[1:] + xor_result[0]

            encrypted_bit += shift_result

        return encrypted_bit

    # Decrypt bit using CBC
    def decrypt_cbc(self):
        '''
        Decrypt:
        1. geser secara wrapping bit-bit dari hasil langkah 1 satu posisi ke kanan
        2. XOR-kan blok cipher Ci dengan K dan dengan hasil XOR sebelumnya
        '''
        decrypted_bit = ""

        if(len(self.key)<128):
           self.key = self.key.zfill(128)
        length_key = len(self.key)

        for i in range(0, len(self.bit), length_key):
            # geser secara wrapping bit-bit dari hasil langkah 1 satu posisi ke kanan
            block = self.bit[i:i+length_key]

            shift_result = block[-1] + block[:-1]
    
            xor_result = decrypt_block(int(shift_result, 2), int(self.key,2))

            # XOR-kan blok cipher Ci dengan K dan dengan hasil XOR sebelumnya
            if i == 0:
                xor_result = xor_result ^ int(IV, 2)
            else:
                xor_result = xor_result ^ int(self.bit[i-length_key:i], 2)
            xor_result = format(xor_result, f'0{length_key}b')

            decrypted_bit += xor_result

        return decrypted_bit

    # Encrypt bit using OFB
    def encrypt_ofb(self):
        '''
        EK(Xi) = (Xi + K) << 1

        r-bit dari hasil enkripsi antrian disalin menjadi elemen posisi paling kanan di antrian
        '''
        encrypted_bit = ""
        for i in range(0, len(self.bit), self.encryption_length):
            if (i == 0):
                queue = format(int(IV, 2), f'0{len(self.key)}b')
            encrypted_queue = format(int(queue, 2) ^ int(self.key, 2), f'0{len(self.key)}b')
            encrypted_queue = encrypted_queue[1:] + encrypted_queue[0]
            block = self.bit[i:i+self.encryption_length]
            xor_result = int(block, 2) ^ int(encrypted_queue[:self.encryption_length], 2)
            xor_result = format(xor_result, f'0{self.encryption_length}b')
            queue = queue[self.encryption_length:] + encrypted_queue[:self.encryption_length]
            encrypted_bit += xor_result
        return encrypted_bit

    # Decrypt bit using OFB
    def decrypt_ofb(self):
        decrypted_bit = ""
        for i in range(0, len(self.bit), self.encryption_length):
            if (i == 0):
                queue = format(int(IV, 2), f'0{len(self.key)}b')
            encrypted_queue = format(int(queue, 2) ^ int(self.key, 2), f'0{len(self.key)}b')
            encrypted_queue = encrypted_queue[1:] + encrypted_queue[0]
            block = self.bit[i:i+self.encryption_length]
            xor_result = int(block, 2) ^ int(encrypted_queue[:self.encryption_length], 2)
            xor_result = format(xor_result, f'0{self.encryption_length}b')
            queue = queue[self.encryption_length:] + encrypted_queue[:self.encryption_length]
            decrypted_bit += xor_result
        return decrypted_bit

    # Encrypt bit using ECB
    def encrypt_ecb(self):
        '''
        EK(P) = (P + K) << 1

        Encrypt:
        1. XOR-kan blok plainteks Pi dengan K 
        2. geser secara wrapping bit-bit dari hasil langkah 1 satu posisi ke kiri
        '''
        encrypted_bit = ""
        for i in range(0, len(self.bit), len(self.key)):
            # XOR-kan blok plainteks Pi dengan K
            block = self.bit[i:i+len(self.key)]
            xor_result = int(block, 2) ^ int(self.key, 2)
            xor_result = format(xor_result, f'0{len(self.key)}b')
            # geser secara wrapping bit-bit dari hasil langkah 1 satu posisi ke kiri
            shift_result = xor_result[1:] + xor_result[0]
            encrypted_bit += shift_result
        return encrypted_bit

    # Decrypt bit using ECB
    def decrypt_ecb(self):
        '''
        Decrypt:
        1. geser secara wrapping bit-bit dari hasil langkah 1 satu posisi ke kanan
        2. XOR-kan blok cipher Ci dengan K
        '''
        decrypted_bit = ""
        for i in range(0, len(self.bit), len(self.key)):
            # geser secara wrapping bit-bit dari hasil langkah 1 satu posisi ke kanan
            block = self.bit[i:i+len(self.key)]
            shift_result = block[-1] + block[:-1]
            # XOR-kan blok cipher Ci dengan K
            xor_result = int(shift_result, 2) ^ int(self.key, 2)
            xor_result = format(xor_result, f'0{len(self.key)}b')
            decrypted_bit += xor_result
        return decrypted_bit

    # Encrypt bit using Counter
    def encrypt_counter(self):
        '''
        EK(Ti) = (Ti + K) << 1

        • Nilai counter harus berbeda dari setiap blok yang dienkripsi. Pada mulanya, 
        untuk enkripsi blok pertama, counter diinisialisasi dengan sebuah nilai. 
        • Selanjutnya, untuk enkripsi blok-blok berikutnya counter dinaikkan
        (increment) nilainya satu (counter = counter + 1). 
        '''
        encrypted_bit = ""
        for i in range(0, len(self.bit), len(self.key)):
            if (i == 0):
                counter = format(int(COUNTER, 2), f'0{len(self.key)}b')
            encrypted_counter = format(int(counter, 2) ^ int(self.key, 2), f'0{len(self.key)}b')
            encrypted_counter = encrypted_counter[1:] + encrypted_counter[0]
            block = self.bit[i:i+len(self.key)]
            xor_result = int(block, 2) ^ int(encrypted_counter, 2)
            xor_result = format(xor_result, f'0{len(self.key)}b')
            counter = format(int(counter, 2) + 1, f'0{len(self.key)}b')
            encrypted_bit += xor_result
        return encrypted_bit

    # Decrypt bit using Counter
    def decrypt_counter(self):
        decrypted_bit = ""
        for i in range(0, len(self.bit), len(self.key)):
            if (i == 0):
                counter = format(int(COUNTER, 2), f'0{len(self.key)}b')
            encrypted_counter = format(int(counter, 2) ^ int(self.key, 2), f'0{len(self.key)}b')
            encrypted_counter = encrypted_counter[1:] + encrypted_counter[0]
            block = self.bit[i:i+len(self.key)]
            xor_result = int(block, 2) ^ int(encrypted_counter, 2)
            xor_result = format(xor_result, f'0{len(self.key)}b')
            counter = format(int(counter, 2) + 1, f'0{len(self.key)}b')
            decrypted_bit += xor_result
        return decrypted_bit

    # Encrypt bit using CFB
    def encrypt_cfb(self):
        '''
        EK(Xi) = (Xi + K) << 1

        r-bit dari hasil enkripsi plaintext menjadi elemen posisi paling kanan di antrian
        '''
        encrypted_bit = ""
        for i in range(0, len(self.bit), self.encryption_length):
            if (i == 0):
                queue = format(int(IV, 2), f'0{len(self.key)}b')
            encrypted_queue = format(int(queue, 2) ^ int(self.key, 2), f'0{len(self.key)}b')
            encrypted_queue = encrypted_queue[1:] + encrypted_queue[0]
            block = self.bit[i:i+self.encryption_length]
            xor_result = int(block, 2) ^ int(encrypted_queue[:self.encryption_length], 2)
            xor_result = format(xor_result, f'0{self.encryption_length}b')
            queue = queue[self.encryption_length:] + xor_result
            encrypted_bit += xor_result
        return encrypted_bit

    # Decrypt bit using CFB
    def decrypt_cfb(self):
        decrypted_bit = ""
        for i in range(0, len(self.bit), self.encryption_length):
            if (i == 0):
                queue = format(int(IV, 2), f'0{len(self.key)}b')
            encrypted_queue = format(int(queue, 2) ^ int(self.key, 2), f'0{len(self.key)}b')
            encrypted_queue = encrypted_queue[1:] + encrypted_queue[0]
            block = self.bit[i:i+self.encryption_length]
            xor_result = int(block, 2) ^ int(encrypted_queue[:self.encryption_length], 2)
            xor_result = format(xor_result, f'0{self.encryption_length}b')
            queue = queue[self.encryption_length:] + block
            decrypted_bit += xor_result
        return decrypted_bit
    
    def encrypt(self):
        ret = ""

        self.start_time = datetime.now()
        # Put padding on bit input
        if self.mode_method == METHOD['CFB'] or self.mode_method == METHOD['OFB']:
            self.extend_bit_by_encryption_length()
        else:
            self.extend_bit_by_key()

        if self.mode_method == METHOD['ECB']:
            # Encrypt plainteks bit
            ret = self.encrypt_ecb()
        elif self.mode_method == METHOD['CBC']:
            # Encrypt plainteks bit
            ret = self.encrypt_cbc()
        elif self.mode_method == METHOD['OFB']:
            # Encrypt plainteks bit
            ret = self.encrypt_ofb()
        elif self.mode_method == METHOD['CFB']:
            # Encrypt plainteks bit
            ret = self.encrypt_cfb()
        elif self.mode_method == METHOD['COUNTER']:
            # Encrypt plainteks bit
            ret = self.encrypt_counter()

        self.end_time = datetime.now()
        return ret
    
    def decrypt(self):
        ret = ""

        self.start_time = datetime.now()
        # Put padding on bit input
        if self.mode_method == METHOD['CFB'] or self.mode_method == METHOD['OFB']:
            self.extend_bit_by_encryption_length()
        else:
            self.extend_bit_by_key()

        if self.mode_method == METHOD['ECB']:
            # Decrypt plainteks bit
            ret = self.decrypt_ecb()
        elif self.mode_method == METHOD['CBC']:
            # Decrypt plainteks bit
            ret = self.decrypt_cbc()
        elif self.mode_method == METHOD['OFB']:
            # Decrypt plainteks bit
            ret = self.decrypt_ofb()
        elif self.mode_method == METHOD['CFB']:
            # Decrypt plainteks bit
            ret = self.decrypt_cfb()
        elif self.mode_method == METHOD['COUNTER']:
            # Decrypt plainteks bit
            ret = self.decrypt_counter()

        self.end_time = datetime.now()
        return ret

    def get_time_execution(self):
        return (self.end_time - self.start_time).total_seconds()
