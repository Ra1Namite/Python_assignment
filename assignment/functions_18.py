#user_input:

n1 = input('enter the string: ').strip()

#main_program:
print('\nGiven string is number?')
y = lambda x : True if x.replace('.','',1).isdigit() else False
z = lambda x : y(x[1:]) if x[0] =='-' else y(x)
print(z(n1))

