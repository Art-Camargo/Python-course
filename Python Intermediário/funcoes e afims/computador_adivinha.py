import random
def computador_joga():
    return random.randint(0, 100)


continua = True
numero = random.randint(0, 100)
print(f'O número é igual a {numero}')
while continua:
    computador = computador_joga()
    if computador != numero: 
        print(computador)
    else:
        continua = not continua
print(f'{numero=} e {computador=}')