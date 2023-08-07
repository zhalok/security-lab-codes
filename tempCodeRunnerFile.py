# def inverse_matrix(mat):
#     det = np.linalg.det(mat)
#     det = int(det)
#     # print("determinent",det)
#     inv = np.linalg.inv(mat)
#     inv = inv*det
#     print(inv)
#     det = modular_inverse(det,26)
#     inv = inv.transpose().astype(int).tolist()
#     for i in range(len(inv)):
#         for j in range(len(inv[i])):
#             inv[i][j] = inv[i][j]%26*det
#             inv[i][j]%=26
#     return inv

#     # print(inv)