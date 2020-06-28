#user input

lst = list()
print('enter item in empty list:')
while True:
    
    x1 = input('enter item or press(quit) to quit: ').strip()
    if x1 =='quit':
        break
    try:
        if x1.isdigit():
            x1 = int(x1)    
        elif eval(x1):
            x1 = eval(x1)
        lst.append(x1)    
    except:
        lst.append(x1)
    


def copy_list(lst):
    
    lst1 = lst.copy()
    return lst1

lst1 = copy_list(lst)
print('\noriginal: ', lst)
print('\ncloned: ', lst1)
 
