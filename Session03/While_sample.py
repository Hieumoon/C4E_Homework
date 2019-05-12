# while True:
#     print('hi')

# while False:
#     print('hi')

# for v in range(10):
#     print("Hi", v)

# dem = 0
# while True:
#     print('hi', dem)
#     dem += 1  # dem = dem + 1
#     if dem >= 10:
#         break
# print('end')

# mat_khau = input('Moi ban nhap pass:')
# while True: # Lenh nhap cu lap lai mai
#     if len(mat_khau) <= 9:
#         mat_khau = input('Do dai mat khau chua du 8 ky tu')
#     else:
#         print(mat_khau)
#         break


# pw = input('nhap pass:')
# while len(pw)<8:
#     pw = input('pass sai, moi nhap pass:')
# print('pass la:',pw)

while True:
    pw = input('nhap pass:')
    if len(pw)>8:
        break