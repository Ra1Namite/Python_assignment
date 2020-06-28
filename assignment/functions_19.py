#user_input:

n = int(input('How many terms?:').strip())

#main_program
from functools import reduce

fib = lambda y: reduce(lambda x, _: x+[x[-1]+x[-2]],
                                range(y-2), [0, 1])

print(f'\nfibonacci series upto {n}: ')
print(fib(n))
