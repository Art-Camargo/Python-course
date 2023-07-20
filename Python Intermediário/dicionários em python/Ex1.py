#adicionar dados em um dicionário em python
d = {}
nome = input(f'Informe o seu Nome: ')

continua = True
while continua:
    idade = input('Informe a sua idade: ')
    if idade.isdigit():
        if int(idade) > 0:
            continua = False
        else:
            print('Inválido')
    else:
        print('Inválido')
d.setdefault('Nome', nome)
d.setdefault('Idade', idade)

print(d)

    
