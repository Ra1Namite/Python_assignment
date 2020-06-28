#user_input:

lst = list()
while True:
    print('enter key, value for dict and "quit" to quit: ')
    x1 = input().strip()
    if x1 =='quit':
        break
    try:
        if x1.isdigit():
            x1 = int(x1)
        elif eval(x1):
            x1 = eval(x1)
    except:
        pass
    x2 = input().strip()
    if x2 =='quit':
        break
    try:
        if x2.isdigit():
            x2 = int(x2)
        elif eval(x2):
            x2 = eval(x2)
    except:
        pass
    x = (x1, x2)
    lst.append(x)
my_dict = {x[0]:x[1] for x in lst}
print('\nDictionary:',my_dict)

#main_program:

def items_sum(my_dict):
    total = 0
    for x in list(my_dict.values()):
        if type(x) == int:
            total += x 
    return total

y = items_sum(my_dict)
print('\nResult:',y)

