#user_input:

my_list = list()
print('Add items in empty tuple')
while True:
    n = input('add tuple item and (quit) to stop: ').strip()
    if n =='quit':
        break
    if n.isdigit():
        n = int(n)
    my_list.append(n)
my_tuple = tuple(my_list)

print('\ntuple: ',my_tuple)

n1 = input('\nitem to remove: ').strip()
if n1.isdigit():
    n1 = int(n1)

#main_program:


def remove_item_tuple(my_tuple, item_to_remove):
    l1 = list(my_tuple)
    if item_to_remove in l1:
        l1.remove(item_to_remove)
    t1 = tuple(l1)
    return t1

y = remove_item_tuple(my_tuple, n1)
print('\nAfter removing item: ')
print(y)