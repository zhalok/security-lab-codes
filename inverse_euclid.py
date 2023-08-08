def inverse_euclid(a, b, x, y):
    if b == 0:
        x = 1
        y = 0
        return a, x, y

    g, x1, y1 = inverse_euclid(b, a % b, x, y)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


def find_p(n):
    p = 2
    while p * p <= n:
        if n % p == 0:
            return p
        p += 1
    return 1


def find_inverse_module(e, phi):
    keys = []
    g, x, y = inverse_euclid(e, phi, 0, 0)

    if g != 1:
        return -1
    else:
        return x % phi


# def big_mod(a,n,mod):
#     # print(n)
#     if n == 0:
#         return 1

#     if n%2 == 0:
#         return (big_mod(a,n//2,mod)%mod*big_mod(a,n//2,mod)%mod)%mod
#     else:
#         return a*(big_mod(a,n-1,mod)%mod)%mod


def big_mod(a, n, mod):
    if n == 0:
        return 1

    if n % 2 == 0:
        x = big_mod(a, n // 2, mod) % mod
        return (x * x) % mod

    else:
        return (a * big_mod(a, n - 1, mod) % mod) % mod


def encrypt(plain_text, public_keys):
    e, n = public_keys
    encrypted = []
    for i in plain_text:
        a = ord(i) - ord("a") + 1
        encrypted_i = big_mod(a, e, n)
        encrypted.append(encrypted_i)
    return encrypted


def decrypt(encrypted_text, private_keys):
    d, n = private_keys
    decrypted = []
    for i in encrypted_text:
        a = big_mod(i, d, n)
        # decrypted_i = chr(a + ord("a") - 1)
        # decrypted += decrypted_i
        decrypted.append(a)

    return decrypted


n = 80780754611
e = 1234571
p = find_p(n)
q = n // p
phi = (p - 1) * (q - 1)
d = find_inverse_module(e, phi)

# print("Private key", d)
plain_text = "tondrabhalona"
public_keys = (e, n)
private_keys = (d, n)

encrypted_text = encrypt(plain_text, public_keys)
print("encrypted text", encrypted_text)
decrypted_text = decrypt(encrypted_text, private_keys)
print("decrypted_text", decrypted_text)
