n = input('enter length of list: ')
lst = []
for i in range(int(n)):
    x,y = input('enter the element in form (x,y) for tuples inside list: ').split(',')
    lst.append((int(x),int(y)))
print('\nSample list:', lst)
result = sorted(lst, key = lambda x : (x[1], x[0]))

print('\nSorted list:',result)
