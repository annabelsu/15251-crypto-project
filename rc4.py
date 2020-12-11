# Implementation of RC4 in Python for CMU's 15-251 final project
# December 2020

def ksa(key):
    S = list(range(256))
    j = 0
    for i in range(len(S)):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    return S

def prga(S):
    i = 0
    j = 0
    while(True):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256 

        yield S[t]

def encrypt(M, K):

    K = [ord(c) for c in K]
    keystream = prga(ksa(K))

    C = []
    for c in M:
        # 02X prepends a 0 to the front if needed
        C.append(chr((ord(c) ^ next(keystream))))

    return "".join(C)

def decrypt(C, K):

    K = [ord(c) for c in K]
    keystream = prga(ksa(K)) # the same keystream

    M = []
    for c in C:
        M.append(chr((ord(c) ^ next(keystream))))

    return "".join(M)
    
# test me out!
K = "everyone should play persona 5" # change me!
M = "if you can read this its too late" # change me!
C = encrypt(M, K)
decrypted = decrypt(C, K)

print(decrypted)
assert(M == decrypted)