#user_input:

lst = list()
print('enter item in empty list:')
while True:
    
    x1 = input('enter word or press(quit) to quit: ').strip()
    if x1 =='quit':
        break
    lst.append(x1)
print('\nSample list:', lst)

#main_program

lst1 = [x for x in lst if len(x)>1 if x[0] == x[-1]]
count = len(lst1)
print('\nResult:',count)