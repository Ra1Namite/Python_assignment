def add_lists(lst1, lst2):
    lst = lst1[:len(lst1) - 1] + lst2
    return f'resulting list : {lst}'

lst1 = []
lst2 = []
n1 = input('enter length for 1st lst: ')
for i in range(int(n1)):
    lst1.append(input('enter list items: '))

n2 = input('enter length for 2nd lst: ')
for i in range(int(n2)):
    lst2.append(input('enter list items: '))
print('\n',lst1)
print('\n',lst2)
y = add_lists(lst1, lst2)
print('\n',y)

