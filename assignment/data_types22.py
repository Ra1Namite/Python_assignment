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
    
print('\nSample list:', lst)


lst.sort()
for x in lst:
    count = lst.count(x)
    
    while count > 1:

        index = lst.index(x)
        lst.remove(lst[index + (count-1)])
        count -= 1
print('\nResult:',lst)


