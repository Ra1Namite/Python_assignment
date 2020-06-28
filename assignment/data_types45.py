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
n3 = input('\nenter element to be indexed: ')
if n3.isdigit():
    n3 = int(n3)
n1 = input('\nenter start index[optional], press (quit) for None: ').strip()
if n1 == 'quit':
    n1 = None
    
else:
    n1 = int(n1)
    n2 = input('enter stop index[optional], press (quit) for None: ').strip()
    if n2 =='quit':
        n2 = None
    else:
        n2 = int(n2)


#main_program:

try:
    if n1 == None:
        index = my_tuple.index(n3)
    elif n2 == None:
        index = my_tuple.index(n3, n1)
    else:
        index = my_tuple.index(n3, n1, n2)
    print('index_valeu: ',index)

except:
    print('element not found')
    
