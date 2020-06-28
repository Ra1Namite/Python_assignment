lst = list()
while True:
    print('enter key, value for dict and "quit" to quit: ')
    x1 = input().strip()
    if x1 =='quit':
        break
    x2 = input().strip()
    if x2 =='quit':
        break
    x = (x1, x2)
    lst.append(x)
dict1 = {x[0]:x[1] for x in lst}



print('\n',dict1)
print('\niterating through dictionary items:')
for item in dict1.items():
    print(item)