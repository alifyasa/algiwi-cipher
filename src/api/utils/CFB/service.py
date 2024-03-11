def caesar_algo(a,b):
    while b>0:
        a.append(a[0])
        del a[0]
        b -= 1
    return a

def xor(a,b):
    sz_a = len(a)
    ret = ""
    for i in range(sz_a):
        if a[i] == b[i]:
            ret += "0"
        else:
            ret += "1"
    return ret

def encrypt_cbc(bit, key):
    initial_vec = [1,0,1,0]
    encrypted_bit = caesar_algo(initial_vec,key)
    encrypted_bit = encrypted_bit[0:len(bit)]
    encrypted_bit = xor(encrypted_bit, bit)
    return encrypted_bit

def decrypt_cbc(bit, key):
    initial_vec = [1,0,1,0]
    decrypted_bit = ""
    return decrypted_bit