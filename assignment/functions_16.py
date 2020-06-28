#user_input
my_list = list()
print('Add integers in empty list')
while True:
    n = input('add list item and (quit) to stop: ').strip()
    if n =='quit':
        break
    if n.isdigit():
        n = int(n)
    my_list.append(n)
print('\nSample list:',my_list)

#Squaring numbers in list:

print('\nSquared numbers in list:')
square = list(map(lambda x: x**2, my_list))
print(square)

#Cube every numbers in list:

print('\nCubed numbers in list:')
cube = list(map(lambda x: x**3, my_list))
print(cube)


