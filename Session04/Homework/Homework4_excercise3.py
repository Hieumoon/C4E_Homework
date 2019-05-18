print("Answer the following algebra question:")
print("If x = 8, then what is the value of 4(x+3) ?")

answers = {
    "choice" : [1,2,3,4],
    "correct" : 4
}

my_answer = int(input('Enter your choice:'))

if my_answer == answers['correct']:
    print("Bingo")
else:
    print(':(')