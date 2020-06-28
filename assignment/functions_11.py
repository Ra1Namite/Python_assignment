y = lambda x : x + 15
n = int(input('enter number for addition: ').strip())
print('\nResult of addition:',y(n))

x = lambda x, y : x * y

n1 = int(input('\nenter number for multiplication: ').strip())
n2 = int(input('enter number for multiplication: ').strip())

print('\nresult of multiplication:',x(n1, n2))

