#fucntion_defination:
def reverse_string(str1):
    str1 = str1[::-1]
    return str1


#user_input:

str1 = input('enter the string: ').strip()
print('String: ',str1)

#fucntion_call:

y = reverse_string(str1)
print('Reversed string: ',y)
