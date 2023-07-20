def multiplicar(multiplicador):
    def multiplica_numero(numero):
        return numero * multiplicador
    return multiplica_numero

duplicar = multiplicar(2)
triplicar = multiplicar(3)
quadruplicar = multiplicar(4)

numero = 10
print(f'Duplicado = {duplicar(numero)}')
print(f'Triplicado = {triplicar(numero)}')
print(f'quadruplicado = {quadruplicar(numero)}')