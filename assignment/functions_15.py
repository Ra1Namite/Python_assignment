#user_input:
my_list = list()
print('Add integers in empty list')
while True:
    n = input('add list item and (quit) to stop: ').strip()
    if n =='quit':
        break
    if n.isdigit():
        n = int(n)
    my_list.append(n)

print('\nSample List:',my_list)

#filetering for even numbers:
print('\nEven numbers form give list:')
even = list(filter(lambda x: x%2 == 0, my_list))
print(even)

#filtering for odd numbers:
print('\nOdd numbers from given list:')
odd = list(filter(lambda x: x%2 != 0, my_list))
print(odd)
