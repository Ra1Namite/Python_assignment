#user_input:
lst = list()
for i in range(2):
    my_list = list()
    print('\nAdd items in empty array')
    while True:
        
        n = input('add array item and (quit) to stop: ').strip()
        if n == 'quit':
            break
        if n.isdigit():
            n = int(n)
        my_list.append(n)
    print('\n',my_list)
    lst.append(my_list)
n1 = lst[0]
n2 = lst[1]
print('\nOriginal Arrays:',n1,n2)

#main_program:
output = list(filter(lambda y: y in n1, n2)) 
print('\nIntersection of arrays:')
print(output)




