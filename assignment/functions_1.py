#function_definition:

def max_number(n1, n2, n3):
    lst = [n1, n2, n3]
    largest = max(lst)
    return largest

#user_input:

n1 = int(input('enter numbers to be compared: ').strip())
n2 = int(input('enter numbers to be compared: ').strip())
n3 = int(input('enter numbers to be compared: ').strip())

#function_call:

x = max_number(n1, n2, n3)
print('\nlargest:',x)
