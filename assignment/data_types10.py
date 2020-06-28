str1 = input('enter the string: ').strip()

lst = [x for x in enumerate(str1) if x[0]%2 == 0]
lst1 = [x[1] for x in lst]
output = ''.join(lst1)
print(output)




