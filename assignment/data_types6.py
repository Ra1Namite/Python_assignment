
str1 = input('enter the string: ').strip()
str2 = str1.replace('!','')
lst1 = str2.split(' ')

if 'not' in lst1 and 'poor' in lst1:
    i1 = lst1.index('not')
    i2 = lst1.index('poor')

    if i1 < i2:
        if str1[-1] == '!':
            lst = lst1[:i1] + ['good!']
        else:
            lst = lst1[:i1] + ['good']
        output = ' '.join(lst)
        print(output) 
    else:
        print(str1)
else:  
    print(str1)

