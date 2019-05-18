print("Answer the following algebra question:")
print("If x = 8, then what is the value of 4(x+3) ?")

answers1 = {
    "choice" : [1,2,3,4],
    "correct" : 4
}

my_answer1 = int(input('Enter your choice:'))
n = 0

if my_answer1 == answers1['correct']:
    print("Bingo")
    n += 1
else:
    print(':(')


print("Estimate this answer (exact calculation not needed):")
print("Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?")
answers2 = {
    "choice" : [1,2,3,4],
    "correct" : 2
}

my_answer2 = int(input('Enter your choice:'))
n = 0

if my_answer2 == answers2['correct']:
    print("Bingo")
    n += 1
else:
    print(':(')

print("You correctly answer",n,"out of 2 questions")