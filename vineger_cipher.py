plain_text = "GEEKSFORGEEKS"
keyword = "TONDRA"

keyword1 = ""
while(len(keyword1)<len(plain_text)):
    for i in range(len(keyword)):
        if len(keyword1) == len(plain_text):
            break
        keyword1 += keyword[i]
print(keyword1)
print(plain_text)



def encrypt(plain_text,keyword):

    encrypted_text = ""
    for i in range(len(plain_text)):
        a = ord(plain_text[i]) - ord('A')
        b = ord(keyword[i]) - ord('A')
        encrypted_val = (a+b)%26
        encrypted_text += chr(encrypted_val + ord('A'))

   
    return encrypted_text


def decrypt(encrypted_text,keyword):
    decrypted_text = ""
    for i in range(len(encrypted_text)):
        a = ord(encrypted_text[i]) - ord('A')
        b = ord(keyword[i]) - ord('A')
        decrypted_val = (a-b)%26
        decrypted_text += chr(decrypted_val + ord('A'))

    print("decrypted text",decrypted_text)
    return decrypted_text


encrypted_text = encrypt(plain_text,keyword1)
decrypted_text = decrypt(encrypted_text,keyword1)

print("encrypted_text",encrypted_text)
print("decrypted_text",decrypted_text)


