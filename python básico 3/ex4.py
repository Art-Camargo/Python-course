end = True
qtd = 0
candidatos = [0, 0, 0, 0, 0, 0]
while end:
    print('1 - Jair messias Bolsonaro')
    print('2 - Luis inácio Lula da Silva')
    print('3 - Aécio Neves')
    print('4 - Boulos')
    print('5 - Branco')
    print('6 - Nulo')
    voto = input('Escolha uma opçao acima (0 para cancelar): ')
    try:
        voto = int(voto)
        while(voto > 6 or voto < 0):
            voto = input('Escolha uma opçao acima (0 para cancelar): ')
            voto = int(voto)
        if voto == 0:
            end = False
        else:
            candidatos[voto - 1] += 1
            qtd += 1
        if qtd == 1:
            maior = candidatos[voto - 1]
        elif candidatos[voto - 1] > maior:
            maior = candidatos[voto - 1]
    except:
        print(f'Você digitou "{voto}" e isso não é um número válido')
print(f'Votos totais === {qtd}')
print(f'Votos totais brancos === {candidatos[4]}')
print(f'Votos totais nulos === {candidatos[5]}')
print(f'Candidato com mais votos === {maior}')