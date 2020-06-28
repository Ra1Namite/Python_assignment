#function_definiton:
def multiply_list(list):
    total = 1
    for x in list:
        total *= x
    return total


#user_input:

my_list = list()
print('Add items in empty list')
while True:
    n = input('add list item and (quit) to stop: ').strip()
    if n =='quit':
        break
    if n.isdigit():
        n = int(n)
    my_list.append(n)
print('\nlist: ',my_list)

#function_call:

y = multiply_list(my_list)
print('\ntotal :',y)
