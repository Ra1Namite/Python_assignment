def add_tags(tag, string):
    return f'<{tag}>{string}</{tag}>'

#user_input:
n1 = input('enter html tag: ').strip()
n2 = input('enter string: ').strip()

x = add_tags(n1, n2)
print(x)
