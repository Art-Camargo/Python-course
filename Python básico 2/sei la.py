from random import *
def rand():

    random = random.range(0, 1)
    random = random.choice()
    return random
escolha = rand()
i = True
while i:
    escolha = rand()
    lista = ['Cara', 'Coroa']
    print(f'{lista[escolha]}')
    a = input('Informe o seu nome: ')
