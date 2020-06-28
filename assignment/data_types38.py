#user_input:


lst = list()
while True:
    print('enter key, value for dict and "quit" to quit: ')
    x1 = input().strip()
    if x1 =='quit':
        break
    if x1.isdigit():
        x1 = int(x1)
    x2 = input().strip()
    if x2 =='quit':
        break
    if x2.isdigit():
        x2 = int(x2)
    x = (x1, x2)
    lst.append(x)
my_dict = {x[0]:x[1] for x in lst}

print('\n',my_dict)


#main_program:

def remove_key(my_dict, element_to_remove):
    if element_to_remove in my_dict:
        my_dict.pop(element_to_remove)
    return my_dict

n = input('\nenter key to be removed:').strip()
if n.isdigit():
    n = int(n)
y = remove_key(my_dict, n) 
print(y)

