name = input('Informe o seu nome: ') or 'Nome não informado'
age = input('Informe a sua idade: ') or 'Idade não informada'
if name != 'Nome não informado' and age != 'Idade não informada':
    print(f'Seu nome é: {name}!', end="\n\n")
    print(f'Seu nome invertido é: {name[-1::-1]}', end="\n\n")
    if ' ' in name:
        print(f'O seu nome: {name} contém espaços!')
    else:
        print(f'O seu nome {name} não contém espaços!')
    print('O seu nome tem %d letras' % len(name)) 
    print(f'A primeira letra do seu nome é: {name[0]}')
    print(f'A última letra do seu nome é {name[-1]}')
    print(f'A sua idade é === {age}')
else:
    print('Desculpe, você deixou campos vazios!')