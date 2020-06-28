string = input('enter the string: ').strip()
result = dict()
for _ in string:
    
    result[_] = string.count(_)
print(result)
