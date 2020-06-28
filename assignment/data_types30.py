def has_key(dict, key):
    lst = list(dict.keys())
    if key in lst:
        return 'given key exist in dictionary'
    else:
        return "key doesn't exist"


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
key = input('enter key: ')


y = has_key(dict1, key)

print(y)
