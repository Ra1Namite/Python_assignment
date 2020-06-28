def sort_list(lst, key):
    lst.sort(key = lambda x: x[key])
    return lst

#user_input:

lst = list()
my_dict = dict()
print('\n initializing dictionary:')
while True:
    print('Enter keys for initializing dictionary:')
    n1 = input('enter dictionary key or (quit) to end:').strip()
    if n1 == 'quit':
        break
    if n1.isdigit():
        n1 = int(n1)
    my_dict[n1] = None
print('\nInitialized dictionary:', my_dict)

while True:
    

    while True:
        my_dict1 = my_dict.copy()

        print('\nEnter values for respective dictionary:')
        for key in my_dict1:
            
            n2 = input(f'enter the value for [{key}] key or press (quit) to quit:').strip()
            if n2 == 'quit':
                break
            if n2.isdigit():
                n2 = int(n2)
            my_dict1[key] = n2
        if n2 == 'quit':
            break
        lst.append(my_dict1)
        

    if n2 == 'quit':
        break
    


print('\nSample list:', lst)

n = input('\nenter key to sort dictionary by:')
if n.isdigit():
    n = int(n)

#function_call:
try:
    y = sort_list(lst, n)
    print('\n Sorted list:', y)
except:
    print('\nenter values of same type')


