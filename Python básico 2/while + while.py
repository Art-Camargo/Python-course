name = 'ARTUR DE CAMARGO'
i = 0
name = name.capitalize()
string = ''
while i < len(name):
    if i == 0:
        string += f'*{name[i]}*'    
    else:
        string += f'{name[i]}*'
    i += 1
print(string)