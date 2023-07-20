
def printa_menu():
    print('1 - Laranja\n2 - Melância\n3 - Abacate')
    op = input('Informe o que quer comprar: ')
    if op.isdigit():
        if int(op) <= 3 and int(op) >= 1:
            return op
    return None

def qtd_frutas():
    ...

        




continua = True
soma = 0
while continua:
    opcao = printa_menu() 
    if opcao is not None:
        qtd = qtd_frutas()
        if opcao == 1:
            ...   
        elif opcao == 2:
            ...
        else:
            ...