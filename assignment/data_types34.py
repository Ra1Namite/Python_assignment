
dicts = list()
for i in range(1,3):
    lst1 = []
    dict1 = {}
    while True:
        print(f'enter key, value for dict{i} and "quit" to quit: ')
        x1 = input().strip()
        if x1 =='quit':
            break
        x2 = input().strip()
        if x2 =='quit':
            break
        x = (x1, x2)
        lst1.append(x)
    dict1 = {x[0]:x[1] for x in lst1}
    dicts.append(dict1)

merge_dict = {**dicts[0], **dicts[1]}
print('\nresulting dictionary')
print(merge_dict)
