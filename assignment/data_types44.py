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

print('\ntuple:',my_tuple)
n1 = int(input('\n enter start index: ').strip())
n2 = int(input('\n enter stop index: ').strip())
n3 = input('\n enter step index[optional], press (quit) for None: ').strip()
if n3 == 'quit':
    n3 = None
else:
    n3 = int(n3)


#main_program:

def slice_tuple(tuple,start, stop, step=None):
    return tuple[start:stop:step]

y = slice_tuple(my_tuple, n1, n2, n3)
print('\nsliced tuple:')
print(y)
