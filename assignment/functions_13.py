#function_definition:
def sort_list(lst):
    lst.sort(key = lambda x: x[1])
    return lst

#user_input:

lst = list()
while True:
    print('\nEnter elements in tuples for list:')
    n1 = input('enter 1st element or (quit) to end:').strip()
    if n1 == 'quit':
        break
    if n1.isdigit():
        n1 = int(n1)
    n2 = input('enter 2nd element or (quit) to end:').strip()
    if n2 == 'quit':
        break
    if n2.isdigit():
        n2 = int(n2)
    lst.append((n1, n2))
print('\nSample list:', lst)
#function_call:
try:
    y = sort_list(lst)
    print('\nsorting by 2nd element of tuple....')
    print('\nSorted list:',y)
except:
    print('\nPlease only enter numbers')


