#function_definition:

def check_prime(n):
    if n==1:
        return False
    elif n==2:
        return True
    else:
        for x in range(2, n):
            if(n % x == 0):
                return False
        return True
    
#user_input:

n = int(input('enter number: ').strip())

#function_call:
print('\nPrint True of prime and False for non-prime:')
y = check_prime(n)
print('\nResult:',y)



