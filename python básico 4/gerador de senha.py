import random
letras = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
letras += letras.lower()
num = '0123456789'
char = '#$%:;[]}'
total = char + num + letras
password = ''
for i in range(8):
    password += random.choice(total)
print(password)