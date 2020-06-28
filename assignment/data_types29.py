def merge_dict(*dicts):
    result_dict = {}
    for x in dicts:
        
        result_dict.update(x)
    return result_dict


n = int(input('no of dictionaries u want to merge: ' ))
dicts = list()
for i in range(n):
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

y = merge_dict(*dicts)
print('resulting dictionary: ')

print(y)
