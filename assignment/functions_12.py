#function_definition:

def multiply(n):
    return lambda x : x * n

#user_input:

n = int(input('enter number:').strip())
n1 = int(input('enter random number:').strip())

#function_call:

x = multiply(n)
result = x(n1)
print('\nresult:',result)


