# Write a function that extracts the even items in a given integer list, named 'get_even_list', takes 1 parameter: l, where l is the given integer list, returns a new list contains only even numbers 

def get_even_list(l):
    even_numbers = []
    for i in l:
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

print(get_even_list([1, 4, 5, -1, 10]))