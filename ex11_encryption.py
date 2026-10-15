# Ex 11: Symmetric (XOR) and Asymmetric (RSA) Encryption
def xor_encrypt(message, key):
    return [ord(ch) ^ ord(key[i % len(key)]) for i, ch in enumerate(message)]

def xor_decrypt(encrypted, key):
    return ''.join(chr(v ^ ord(key[i % len(key)])) for i, v in enumerate(encrypted))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

message = input("Enter message: ")
key = input("Enter symmetric key: ")
encrypted_xor = xor_encrypt(message, key)
decrypted_xor = xor_decrypt(encrypted_xor, key)

p, q = 61, 53
n = p * q
phi = (p - 1) * (q - 1)
e = 17
d = mod_inverse(e, phi)

rsa_encrypted = [pow(ord(ch), e, n) for ch in message]
rsa_decrypted = ''.join(chr(pow(v, d, n)) for v in rsa_encrypted)

print("\n----- SYMMETRIC ENCRYPTION (XOR) -----")
print("Original Message :", message)
print("Encrypted Data :", encrypted_xor)
print("Decrypted Message:", decrypted_xor)
print("\n----- ASYMMETRIC ENCRYPTION (RSA) -----")
print("Public Key :", (e, n))
print("Private Key :", (d, n))
print("Encrypted Data :", rsa_encrypted)
print("Decrypted Message:", rsa_decrypted)
