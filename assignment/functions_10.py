#function_definition:

def print_even_numbers(lst):
    l1 = [x for x in lst if x%2 == 0]
    return l1

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

print('\nSample List:',my_list)

#function_call:

y = print_even_numbers(my_list)

print('\nlist with even numbers only:',y)
