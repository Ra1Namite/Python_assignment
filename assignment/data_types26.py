def concatinate(list, string):
    lst = [string+str(x) for x in list]
    return lst

#user_input:

lst = list()
print('enter item in empty list:')
while True:
    
    x1 = input('enter word or press(quit) to quit: ').strip()
    if x1 =='quit':
        break
    lst.append(x1)
print('\nSample list:', lst)

n1 = input('give string: ').strip()

x = concatinate(lst, n1)
print('\nResult:',x)





