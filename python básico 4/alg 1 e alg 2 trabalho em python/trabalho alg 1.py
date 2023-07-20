import os
RED   = "\033[1;31m" 
RESET = "\033[0;0m"
GREEN = "\033[0;32m"
def printa_menu():
    print(' 1 - Cadastrar metal\n 2 - Remover metal\n', \
          '3 - Quantidade de metais estocados por tipo de metais\n', \
          '4 - Tipos de metais sem estoque\n', '5 - Quantidade total de metais de metais estocados\n'\
          , '6- FIM')
    op = input('Informe uma opção acima: ')
    try:
        op = int(op)
        return op
    except:
        return 0
    
def printa_atuais(qtd_metais, tipos_metais):
    print(GREEN + 'QUANTIDADE,   TIPO' + RESET)
    for i in range(5):
        print(f'     {qtd_metais[i]}         {tipos_metais[i]}')
    print('\n\n')

def cadastra_user(qtd_metais, tipos_metais, index):
    print(f'Cliente com o id = {index}')
    tipo = input('Informe qual o tipo do metal: ')
    while tipo != '3' and tipo != '2' and tipo != '1':
        print(RED + 'INVÁLIDO!!!' + RESET, end = "\n")
        tipo = input('Informe qual o tipo do metal: ')
    tipos_metais[index] = tipo
    qtd = input('Informe a quantidade de metais estocados do produto: ')
    while not qtd.isdigit() or '-' in qtd:
        print(RED + 'INVÁLIDO!!!' + RESET, end = "\n")
        qtd = input('Informe a quantidade de metais estocados do produto: ')
    qtd_metais[index] = qtd 

def remove_metal(qtd_metais, tipos_metais):
    while True:
        indice_remote = input('Informe qual o id do metal que deseja remover: ')
        try:
            indice_remote = int(indice_remote)
            if indice_remote < 5 and indice_remote >= 0:
                if tipos_metais[indice_remote] == '-':
                    print('Código de metal não cadastrado!')
                else:
                    qtd_metais[indice_remote] = '-'
                    tipos_metais[indice_remote] = '-'
                return
            else:
                print(RED + 'Opção Inválida!!!!' + RESET)
        except:
            print(RED + 'TypeERROR!!!' + RESET)
def qtd_por_tipos(qtd_metais, tipos_metais):
    type_metal_aux = input('Informe qual o tipo de metal deseja buscar: ')
    if type_metal_aux != '3' and type_metal_aux != '1' and type_metal_aux != '2':
        print('Opção inválida!')
        return
    counter = 0
    for tipos in range(5):
        if tipos_metais[tipos] == type_metal_aux:
            counter += int(qtd_metais[tipos])
    os.system("cls")
    print(f'Tipo Escolhido: {type_metal_aux}')
    return counter


def tipos_sem_estoque(qtd_metais, tipos_metais, tipo_sem, todos_tem):
    if tipo_sem not in tipos_metais:
        print('O tipo {} está sem estoque'.format(tipo_sem))
    else:
        todos_tem += 1

def qtd_total_metais(qtd_metais):
    soma = 0
    for total in qtd_metais:
        if '-' not in total:
            soma += int(total)
    return soma

qtd_metais = ['-', '-', '-',  '-', '-']
tipos_metais = ['-', '-', '-', '-', '-']
continua = True
index = 0
while continua:
    printa_atuais(qtd_metais, tipos_metais)
    opcao = printa_menu()
    os.system("cls")
    if opcao == 1:
        try:
            index = tipos_metais.index("-")
            cadastra_user(qtd_metais, tipos_metais, index)
        except:
            print('Não há mais clientes para cadastrar!!!!')
    elif opcao == 2:
        remove_metal(qtd_metais, tipos_metais)
    elif opcao == 3:
        print(f'Total do tipo escolhido: {qtd_por_tipos(qtd_metais, tipos_metais)} metais')
    elif opcao == 4:
        todos_tem = 0
        tipos_sem_estoque(qtd_metais, tipos_metais, '1', todos_tem)
        tipos_sem_estoque(qtd_metais, tipos_metais, '2', todos_tem)
        tipos_sem_estoque(qtd_metais, tipos_metais, '3', todos_tem)
        if todos_tem == 3:
            print('Todos os tipos possuem estoque!!!')
    elif opcao == 5:
        print(f'Quantidade total de metais = {qtd_total_metais(qtd_metais)}')
    elif opcao == 6:
        print('Programa finalizado. Have a good day')
        continua = not continua
    else:
        print(RED + 'ERROR! ' + RESET + 'OPÇÃO INVÁLIDA NO MENU.')
        
