end = True
soma = 0
while end:
    print('Cachorro quente, código 0: ')
    print('Uva, código 1: ')
    print('Laranja, código 2: ')
    print('Melão, código 3: ')
    pick = int(input('Informe o código do produto que deseja comprar: '))
    while pick > 3 or pick < 0:
        pick = int(input('Informe o código do produto que deseja comprar: '))
    qtd = int(input('Informe a quantidade: '))
    while qtd < 0:
        qtd = int(input('Informe a quantidade: '))
    if pick == 0:
        soma += qtd * 1.25
    elif pick == 1:
        soma += qtd * 2.25
    elif pick == 2:
        soma += qtd * 1.35
    elif pick == 3:
        soma += qtd * 3.99
    fim = input('Você deseja comprar mais? digite sim ou não: ')
    fim = fim.lower()
    while fim != 's' and fim != 'sim' and fim != 'n' and fim != 'não' and fim != 'nao':
        fim = input('Você deseja comprar mais? digite sim ou não: ')
        fim = fim.lower()
    if fim == 'n' or fim == 'não' or fim == 'nao':
        end = False
    else:
        end = True
        print(f'Valor total === {soma:.2f}')
        