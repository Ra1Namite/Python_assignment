def insert_string_middle(str1, str2):
    x = str1[:int(len(str1)/2) ] + str2 + str1[int(len(str1)/2):]
    return x

n1 = input('enter string: ').strip()
n2 = input('enter string to be inserted in middle: ').strip()


y = insert_string_middle(n1, n2)
print('\nResult: ',y)

