def titulacao(sexo, nome):
    print('Doutor')
    print('Mestre')
    x = input('Informe a sua titularidade: ')
    x = x.lower()
    while x != 'doutor' and x != 'mestre':
        x = input('Informe a sua titularidade: ')
        x = x.lower()
    if sexo == 'f':
        if x == 'doutor':
            print(f'Doutora {nome}')
        else:
            print(f'Mestra {nome}')
    else:
        if x == 'doutor':
            print(f'Doutor {nome}')
        else:
            print(f'Mestre {nome}')
name = input('Enter with your name: ')
try:
    name = float(name)
    print(f'"{name}" é um número, não um nome!')
except:
    print('M - Masculino')
    print('F - Feminino')
    sex = input('Informe uma opção: ')
    sex = sex.lower()
    while sex != 'm' and sex != 'f':
        sex = input('Informe uma opção válida: ')
        sex = sex.lower()
    titulacao(sex, name)