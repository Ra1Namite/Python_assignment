
#function_definition:

def sum_list(l1):
    return sum(l1)

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

y = sum_list(my_list)
print('\nTotal sum: ',y)

