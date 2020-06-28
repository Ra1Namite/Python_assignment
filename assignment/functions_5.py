#function_definition:
def factorial(number):
    total = 1
    if number == 0:
        total = 1
    elif n >= 0:
        for i in range(1,number+1):
            total *= i
    else:
        return '\nplease enter positive number'
    return total

#user_input:

n = int(input('enter the number: ').strip())



#function_call:

y = factorial(n)
print('factorial:',y)


