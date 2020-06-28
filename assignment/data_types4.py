str1 = input('enter 1st string: ').strip()
str2 = input('enter 2nd string: ').strip()

str3 = str2[:2] + str1[2:]
str4 = str1[:2] + str2[2:]
lst = [str3, str4]
output = ' '.join(lst)
print(output)
