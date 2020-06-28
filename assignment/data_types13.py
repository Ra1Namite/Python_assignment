str1 = input('enter the words: ').strip()
words = str1.split(',')


x = sorted(words)



output = ', '.join(x)
print('\nSorted result:',output)
