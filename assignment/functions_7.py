#function_definition:

def letter_case_numbers(string):
    upper_count = 0
    lower_count = 0
    for letter in string:
        if letter.isupper():
            upper_count += 1
        elif letter.islower():
            lower_count += 1
    return upper_count, lower_count

#user_input:

str1 = input('enter the string: ').strip()

#function_call:

x, y = letter_case_numbers(str1)

print('\nNo. of Upper case characters:',x)
print('\nNo. of Upper case characters:',y)
