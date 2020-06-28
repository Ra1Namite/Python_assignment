str1 = input('enter the string: ').strip()
str2 = str1[-1] + str1[1:len(str1)-1] + str1[0]
print(str2)