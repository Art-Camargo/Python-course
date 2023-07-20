def multiplica_numeros(*args):
    acumula = 1
    args = list(args)
    for i in range(len(args)):
        acumula *= int(args[i])
    return acumula      
def impar_ou_par(resposta):
    if resposta %2 == 0:
        return 'par'
    else:
        return 'ímpar'


numeros = 3, 5, 3
resposta = multiplica_numeros(*numeros)
tipo = impar_ou_par(resposta)
print(f'O resultado da multiplicação {resposta} é {tipo}')