# Write a function that removes the dollar sign ('$') in a string, named 'remove_dollar_sign', takes 1 arguments: s, where s is the input string, returns the new string with no dollar sign in it. 

def remove_dollar_sign(s):
    new_s = s.replace("$","")
    return new_s

s = input('Enter the string containing $: ')

print(remove_dollar_sign(s))