
#function definition:

def longest_word(words):
    lst2 = [len(x) for x in words]
    longest= max(lst2)
       
    return longest

#user_input:

lst = list()
print('enter item in empty list:')
while True:
    
    x1 = input('enter word or press(quit) to quit: ').strip()
    if x1 =='quit':
        break
    lst.append(x1)
print('\nSample list:', lst)

#function_call

x = longest_word(lst)
print('\nLongest length:',x)