str1 = input('enter the string: ').strip()
n = int(input('enter the index to remove: '))
if len(str1) > 0:
    str1 = str1[:n] + str1[n+1:]
print(str1)
