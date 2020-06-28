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
#main_program:

length = len(my_tuple)
print('\nlength of tuple is: ',length)
