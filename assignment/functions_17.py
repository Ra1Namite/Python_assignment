#user_input:

n1 = input('enter the string: ').strip()
n2 = input('enter character to check the start of string: ').strip()

#main_program
print(f'\nDoes a string ({n1}) starts with a character ({n2})? ')
x = lambda n1, n2: True if n1.startswith(n2) else False 
print(x(n1, n2))


