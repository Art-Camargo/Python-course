i = 0
while(i < 10):
    name = input('Informe o seu nome: ')
    try:
        name = float(name)
        print(f'Você digitou {name} e isso não é um nome!')
    except:
        print(f'O seu nome é {name} e contem {len(name)} letras!')
        if ' ' not in name:
            print(f'O seu nome com a função de primeira letra maiúscula: {name.capitalize()}')