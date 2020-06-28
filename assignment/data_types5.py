str1 = input('enter the string: ').strip()
if len(str1) > 2:
    
    if str1[-3:] != 'ing':
        str1 = str1 + 'ing'
    else:
        str1 = str1 + 'ly'
print(str1)
    