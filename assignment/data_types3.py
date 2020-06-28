string = input('enter the string: ').strip()
lst1 = list(string)
lst2 = lst1[:]

for _ in lst1[1:]:
    if _ == lst1[0]:
        lst2[lst2[1:].index(_) + 1] = '$'
output = ''.join(lst2)
print(output)


               
    