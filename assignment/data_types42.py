#user_input:

my_list = list()
while True:
    n = input('enter list item and (quit) to stop: ')
    if n == 'quit':
        break
    if n.isdigit():
        n = int(n)
    my_list.append(n)

#main_program:
print('\n',my_list)
def conversion(list):
    return tuple(list)
print('\nConversion of list to tuple: ')

y = conversion(my_list)
print(y)
