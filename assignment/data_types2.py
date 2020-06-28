string = input('enter the string: ')
string = string.strip()
output = ''
if len(string)<2:
    print('Empty String')
else:
    output = string[:2] + string[-2:]
    print(output)


