# Implementation of TEA in Python for CMU's 15-251 final project
# December 2020

def encrypt(M, K):
    delta = int("9E3779B9", 16)
    (L, R) = M[0], M[1]
    sum = 0
    for i in range(0, 32):
        sum += delta
        L += ((R << 4) + K[0]) ^ (R + sum) ^ ((R >> 5) + K[1])
        R += ((L << 4) + K[2]) ^ (L + sum) ^ ((L >> 5) + K[3])
    
    return [L, R]


def decrypt(C, K):
    delta = int("9E3779B9", 16)
    (L, R) = C[0], C[1]
    sum = delta * 32
    for i in range(0, 32):
        R -= ((L << 4) + K[2]) ^ (L + sum) ^ ((L >> 5) + K[3])
        L -= ((R << 4) + K[0]) ^ (R + sum) ^ ((R >> 5) + K[1])
        sum -= delta
    
    return [L, R]


# test me out!
M = [12543,225324] # change me!
K = [12,22354,3543,420] # change me!
C = encrypt(M, K)
decrypted = decrypt(C, K)

print(decrypted)
assert(M == decrypted)