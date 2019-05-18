
# n = 48

# so_chia = 2

# while True: 
#     if n % so_chia == 0:
#         kq = n / so_chia
#         print(so_chia)
#         n = kq
#     else:
#         so_chia += 1
#     if n == 1:
#         break 



# n = 48

# so_chia = 2

# while n > 1: 
#     if n % so_chia == 0:
#         n = n / so_chia
#         print(so_chia)
#         # n = kq
#     else:
#         so_chia += 1
    


# n = 48

# so_chia = 2

# while n > 1: 
#     if n % so_chia == 0:
#         n = n / so_chia
#         print(so_chia)
#         ls.append(so_chia)
#         # n = kq
#     else:
#         so_chia += 1
# print(ls)



n = int(input('nhap so can tinh:'))

so_chia = 2

ls = []
while n > 1: 
    if n % so_chia == 0:
        n = n / so_chia
        print(so_chia)
        ls.append(so_chia)
        # n = kq
    else:
        so_chia += 1

print(ls)