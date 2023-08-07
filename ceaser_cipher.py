encrypted_text = "ftqzqjfwuxxqdmbbiuxxoaynuzqoxagpymotuzqxqmdzuzsuafmzpnxaowotmuz"
encrypted_text.lower()


for k in range(0,26):
    decrypted_text = ""
    for i in range(0,len(encrypted_text)):
        old_char = encrypted_text[i]
        old_char_ord = ord(old_char) - ord('a')
        new_char_ord = ((old_char_ord-k)%26+26)%26
        new_char = chr(new_char_ord + ord('a'))
        decrypted_text += new_char
    print(decrypted_text)



