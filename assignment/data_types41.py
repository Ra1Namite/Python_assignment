my_tuple = ()
print('Add items in empty tuple')
while True:
    n = input('\nadd tuple item and (quit) to stop: ').strip()
    if n =='quit':
        break
    
    my_tuple += (n,)

print(my_tuple)

print('\nconversion to string: ')
print(''.join(my_tuple))



