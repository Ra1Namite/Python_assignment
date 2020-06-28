#function_definition:

def number_in_range(start, end, number):
    if number in range(start, end +1):
        return f'{number} in a range'
    else:
        return f'{number} not in a range'


#user_input:

n1 = int(input('enter start of range: ').strip())
n2 = int(input('enter end of range: ').strip())
n3 = int(input('enter number to be tested: ').strip())

#function_call:

y = number_in_range(n1, n2, n3)

print(y)
