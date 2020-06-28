str1 = input('enter sentence: ').strip()
words = str1.split()
total_counts = dict()
for word in words:
    if word not in total_counts:
        
        total_counts[word] = words.count(word)

print('\nResult:',total_counts)



