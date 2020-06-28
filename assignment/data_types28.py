def add_dict_key(dict1, dict2):
    dict1.update(dict2)
    return dict1

lst1 = list()
lst2 = list()
while True:
    print('enter key, value for dict1 and "quit" to quit: ')
    x1 = input().strip()
    if x1 =='quit':
        break
    x2 = input().strip()
    if x2 =='quit':
        break
    x = (x1, x2)
    lst1.append(x)

while True:
    print('enter key, value for dict2 and "quit" to quit: ')
    x1 = input().strip()
    if x1 =='quit':
        break
    x2 = input().strip()
    if x2 =='quit':
        break
    x = (x1, x2)
    lst2.append(x)


dict1 = {x[0]:x[1] for x in lst1}
dict2 = {x[0]:x[1] for x in lst2}
y = add_dict_key(dict1, dict2)
print('adding dictionary keys: ')
print(y)

