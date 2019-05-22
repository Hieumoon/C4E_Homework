# def say_hi():
#     print('hi')

# say_hi()
# say_hi()

# def add_two_number():
#     a = int(input('nhap so thu nhat:'))
#     b = int(input('nhap so thu hai:'))

#     print('tong hai so la:', a+b)

# add_two_number()

# def add_two_number(a,b):
#     print((a,b))
#     print((x,y))
#     # a = int(input('nhap so thu nhat:'))
#     # b = int(input('nhap so thu hai:'))

#     print('tong hai so la:', x+y)
# x = 50
# y = 7
# add_two_number(x,y)



# def abs_of_number(a):
#     if a > 0:
#         return a
#         print('tri tuyet doi la:'. a)
#     else:
#         return -a
#         print('tri tuyet doi la:', -a)
#     print('tri tuyet doi la:', a)

# x = abs_of_number(-12)
# tong = 12 + abs_of_number(-12)


# def evaluate(a,b,o):
#     if o == '+':
#         return a + b
#     if o == '-':
#         return a-b
#     if o == '*':
#         return a*b
#     if o == '/':
#         return a/b
# print(evaluate(1,3,'-'))




def evaluate(a,b,o):
    if o == '+':
        return a + b
    if o == '-':
        return a-b
    if o == '*':
        return a*b
    if o == '/':
        return a/b
def eval_expression(s):
    a = int(s[0])
    b = int(s[2])
    o = int(s[1])
    return evaluate(a,b,o)

while True:
    s = input('nhap bieu thuc:')
    

