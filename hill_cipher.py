import re
import numpy as np

plain_text = "tondrabhalona"
keyword = [[1, 2, 0], [0, 1, 0], [0, 0, 1]]

det = np.linalg.det(keyword)


def text_to_arr(text):
    text_arr = []
    for i in text:
        text_arr.append(ord(i) - ord("a"))

    return text_arr


def arr_to_text(arr):
    text = ""
    for i in arr:
        a = chr(i + ord("a"))
        text += a
    return text


def postprocessing(segments):
    segments = np.array(segments)
    segments = segments.flatten()
    text = arr_to_text(segments)
    return text


def preprocessing(text):
    text = re.sub(r"[ ,.]", "", text)
    text = text.lower()
    text_arr = text_to_arr(text)
    return text_arr


def extended_euclid(a, b, x, y):
    if b == 0:
        x = 1
        y = 0
        return a, x, y
    g, x1, y1 = extended_euclid(b, a % b, x, y)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


def modular_inverse(a, n):
    g, x, y = extended_euclid(a, n, 0, 0)
    if g != 1:
        return -1
    else:
        return x % n


# def inverse_matrix(mat):
#     inverse_matrix = [[0,0,0] for i in range(len(mat))]

#     for i in range(len(mat)):
#         for j in range(len(mat[i])):
#             new_mat = []
#             for k in range(len(mat)):
#                 for l in range(len(mat[k])):
#                     if k != i and l != j:
#                         new_mat.append(mat[k][l])

#             new_mat = np.array(new_mat).reshape(2,2)
#             det = np.linalg.det(new_mat)
#             inverse_matrix[i][j] = ((-1)**(i+j))*int(det)
#     # print("inverted matrix before dividing with determinent",inverse_matrix)
#     det = np.linalg.det(mat)
#     # det = int(det)
#     # print("determinent",det)
#     inverse_matrix = np.array(inverse_matrix).transpose().tolist()
#     for i in range(len(inverse_matrix)):
#         for j in range(len(inverse_matrix[i])):
#             inverse_matrix[i][j] = inverse_matrix[i][j]%26*modular_inverse(det,26)
#             inverse_matrix[i][j]%=26

#     return inverse_matrix


def inverse_matrix(mat):
    det = np.linalg.det(mat)
    det = int(det)

    inv = np.linalg.inv(mat)
    inv = inv * det
    print(inv)
    det = modular_inverse(det, 26)

    for i in range(len(inv)):
        for j in range(len(inv[i])):
            inv[i][j] = inv[i][j] % 26 * det
            inv[i][j] %= 26
    return inv


def segmentize(text, segment_size):
    segments = []
    for i in range(0, len(text), segment_size):
        sub_text = text[i : i + segment_size]
        segments.append(sub_text)
    return segments


def add_padding(segment, padd_len):
    for i in range(padd_len):
        segment.append(0)
    return segment


def matrix_mul(segment, keyword):
    segment = np.array(segment)
    keyword = np.array(keyword)

    lst = np.matmul(keyword, segment)
    lst %= 26

    return lst.astype(int).tolist()


def encrypt(plain_text, keyword):
    segments = segmentize(plain_text, len(keyword[0]))

    for i in range(len(segments)):
        segments[i] = add_padding(segments[i], len(keyword) - len(segments[i]))

    encrypted_segments = []
    for i in range(len(segments)):
        encrypted_segments.append(matrix_mul(segments[i], keyword))
    return encrypted_segments


def decrypt(encrypted_segments, keyword):
    inverse_keyword = inverse_matrix(keyword)
    decrypted_segments = []
    for i in range(len(encrypted_segments)):
        decrypted_segments.append(matrix_mul(encrypted_segments[i], inverse_keyword))
    return decrypted_segments


inversed_matrix = inverse_matrix(keyword)
print(inversed_matrix)

# plain_text = preprocessing(plain_text)

# encrypted_segments = encrypt(plain_text,keyword)
# decrypted_segments = decrypt(encrypted_segments,keyword)
# # print(decrypted_segments)
# flattened = postprocessing(decrypted_segments)

# print(flattened)
