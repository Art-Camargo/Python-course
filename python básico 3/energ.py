end = True
bebe = 0
nao_bebe = 0
aux = 0
entrevistados = 0
acm = 0
maior = 0
while end:
    age = int(input('Informe a sua idade: '))
    while age < 0:
        age = int(input('Informe a sua idade (maior que 0): '))
    if age == 0:
        end = False
    else:
        escolha = input('Você bebe energético? ')
        escolha = escolha.lower()
        while escolha != 's' and escolha != 'sim' and escolha != 'n' and escolha != 'não' and escolha != 'nao':
            escolha = input('Você bebe energético? ')
            escolha = escolha.lower()
        if escolha == 's' or escolha == 'sim':
            bebe += 1
            if aux == 0:
                maior = age
            elif age > maior:
                maior = age
            qtd = int(input('Quantos energéticos você bebe? '))
            acm += qtd
        else:
            nao_bebe += 1
        entrevistados += 1
print(f'Maior idade dos que bebem energético === {maior}')
print(f'Quantidade total de entrevistados === {entrevistados}')
print(f'Quantidade de pessoas que bão bebem energético === {nao_bebe}')
if bebe == 0:
    print('Média === 0')
else:
    print(f'Média do consumo de energético === {acm / bebe:.2f}')
print(f'Toal de pessoas que bebem energético === {bebe}')