#function_definition:

def unique_list(list):
    lst = []
    for item in list:
        if item not in lst:
            lst.append(item)
    return lst

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

y = unique_list(my_list)
print('\nResult List:',y)
