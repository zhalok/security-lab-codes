tabble = {
    "0011": ["00", "11"],
    "0100": ["00", "01"],
    "1111": ["00", "10"],
    "0001": ["00", "11"],
    "1010": ["01", "00"],
    "0110": ["01", "01"],
    "0101": ["01", "10"],
    "1011": ["01", "11"],
    "1110": ["10", "00"],
    "1101": ["10", "01"],
    "0100": ["10", "10"],
    "0010": ["10", "11"],
    "0111": ["11", "00"],
    "0000": ["11", "01"],
    "1001": ["11", "10"],
    "1100": ["11", "11"],
}

hex_map = {}

for i in range(10):
    hex_map[str(i)] = i

for i in range(6):
    hex_map[chr(ord("a") + i)] = 10 + i


def hex_to_bin_conv(hex_val):
    bin_val = ""
    for i in range(4):
        bin_val += str(hex_val % 2)
        hex_val //= 2

    return bin_val[::-1]


def bin_to_hex_conv(bin_val):
    hex_val = 0
    for i in bin_val:
        hex_val *= 2
        hex_val += int(i)

    return hex_val


def hex_remap(hex):
    items = hex_map.items()
    items = list(items)
    for i in range(len(items)):
        if items[i][1] == hex:
            return items[i][0]
    return -1


def decrypt(cipher_text):
    plain_text = ""

    for i in cipher_text:
        val = hex_map[i]
        bin_val = hex_to_bin_conv(val)
        row = tabble[bin_val][0]
        col = tabble[bin_val][1]
        # print(type(row))
        plain = row + col
        # print(type(plain))
        plain_val = bin_to_hex_conv(plain)
        plain_text += str(hex_remap(plain_val))

    return plain_text


cipher_text = "77ba"
plain_text = decrypt(cipher_text)
print(plain_text)
