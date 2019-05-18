count_dict = {}                                     # Create an empty dictionary of counts  
s = input("Enter your sentence here:")              # Enter the input
s = s.lower()                                       # Make all the letter lower cases

for i in s:                      # Iterate through the characters of the string, one character at a time 
    if i in count_dict:
        count_dict[i] +=1        # Count the number of times each letter occurs. Keep the count in a dictionary
    else:
        count_dict[i] = 1

letter_items = list(count_dict.items()) # Type conversion function "list" to change items from a dictionary into a list
letter_items.sort()                     # Display the frequency table in alphabetical order
print(letter_items) 

