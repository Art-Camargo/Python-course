import os


def inverte_num(numero):
    return numero[::-1]


while True:
    numero = input('Informe um número: ')
    os.system("cls")
    if numero.isdigit():
        print(f'Número invertido = {inverte_num(numero)}')
        break
    else:
        print('Não é um número!')
