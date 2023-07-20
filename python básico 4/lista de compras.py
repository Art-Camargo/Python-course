lista = []
while True:
    print('\t\tAdicionar, Apagar, Listar')
    op = input('\t\tInforme uma opção acima: ')
    op = op.capitalize()
    while op != 'Adicionar' and op != 'Apagar' and op != 'Listar':
        op = input('\t\tInforme uma opção acima:')
        op = op.capitalize()
    if op == 'Adicionar':
        aux = input('Adicione algo para a lista de compras: ')
        aux = aux.capitalize()
        lista.append(aux)
    elif op == 'Apagar':
        for i, j in enumerate(lista):
            print('\t', i, j)
        apagar = input('Informe qual você quer apagar, por número: ')
        try:
            apagar = int(apagar)
            try:
                lista.pop(apagar)
            except:
                print('opção inválida: ')
        except TypeError:
            print('Informe um número inteiro')
            print('Opção inválida: ')
    else:
        for i, j in enumerate(lista):
            print('\t', i, j)