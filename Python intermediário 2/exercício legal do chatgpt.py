import os
from time import sleep
def exibir_e_retornar_menu():
    print("===== Gerenciador de Tarefas =====")
    print("1. Adicionar Tarefa\n2. Listar Tarefas")
    print("3. Marcar Tarefa Como Conclída")
    print("4. Excluir Tarefa\n5. Finalizar programa")
    print("===============================")
    op = input('Informe uma opção acima: ')
    if not op.isdigit():
        return None
    elif int(op) > 5 or int(op) < 1:
        return None
    return int(op)

def add_tarefa(url):
    Tarefa_adicionar = input('Informe a sua tarefa: ')
    if not Tarefa_adicionar:
        print('Não é possível adicionar tarefas em branco')
    else:
        try:
            with open(url, 'a+') as arquivo:
                if Tarefa_adicionar.capitalize in arquivo.readlines():
                    print('Tarefa já adicionada')
                else:
                    arquivo.writelines(f'{Tarefa_adicionar.capitalize()}\n')
        except FileNotFoundError:
            print('Arquivo não encontrado.')

def listar_tarefas(url):
    try:
        with open(url, 'r') as arquivo:
            for index, tarefa in enumerate(arquivo.readlines()):
                  if tarefa:
                      print(f'{index}: {tarefa}', end="")
        temporizador()
        return True
    except:
        return False
    
def temporizador():
    for segundos in range(5, 0, -1):
            print(f'Aguarde ({segundos}) segundos')
            sleep(1)
                
def marcar_concluida(url, GREEN, RESET):
    if listar_tarefas(url):
        print()
        try:
            with open(url, 'r') as arquivo:
                linhas = arquivo.readlines()
                concluida = int(input('Informe qual dessas opções você deseja marcar como concluída: '))  
            if concluida > len(linhas) - 1 or concluida < 0:
                print('Não há tarefas para marcar como concluída nesse código')
            else:
                with open(url, 'r+') as arquivo:
                    sleep(1)
                    for index, linha in enumerate(linhas):
                        if linha:
                            if int(index) == concluida:
                                if '-> (concluída)' not in linha:
                         
                                    print('A Tarefa ' + GREEN + f'({linha.strip()}) ' + RESET +  'foi concluída com sucesso.')
                                    arquivo.writelines(f'{linha.strip()} -> (concluída)\n')  # Adiciona '\n' para criar uma nova linha
                                else:
                                    print('Tarefa já concluída')
                                    arquivo.writelines(f'{linha}')
                            else:
                                arquivo.writelines(f'{linha}')
                
        except FileNotFoundError:
            print('Arquivo não encontrado.')
        except ValueError:
            print('Valor inválido. Certifique-se de fornecer um número inteiro para marcar como concluída.')

def excluir_tarefa(url):
    if listar_tarefas(url):
        print()
        try:
            with open(url, 'r') as arquivo:
                linhas_arq = arquivo.readlines()
                tarefa_excluida = int(input('Informe qual dessas opções você deseja marcar como concluída: '))  
            if tarefa_excluida > len(linhas_arq) - 1 or tarefa_excluida < 0:
                print('Não há tarefas para marcar como concluída nesse código')
            else:
                with open(url, 'r+') as arquivo:
                    for index, sublinha in enumerate(linhas_arq):
                        if int(index) != tarefa_excluida and sublinha:
                            arquivo.writelines(f'{sublinha.strip()}\n')
        except FileNotFoundError:
            print('Arquivo não encontrado.')
        except ValueError:
            print('Valor inválido. Certifique-se de fornecer um número inteiro para excluir alguma tarefa.')

def main():
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    url = 'Tarefas.txt'
    continua = True
    while continua:
        opcao = exibir_e_retornar_menu()
        os.system("cls")
        if opcao is None:
            print('Opção inválida')
        elif opcao == 1:
            add_tarefa(url)
        elif opcao == 2:
            listado = listar_tarefas(url)
            if listado is False:
                print('Erro ao abrir o arquivo')
        elif opcao == 3:
            marcar_concluida(url, GREEN, RESET)
        elif opcao == 4:
            excluir_tarefa(url)
        else:
            continua = False
            print('Programa finalizado e as suas tarefas foram armazenadas no Tarefas.txt')
main()