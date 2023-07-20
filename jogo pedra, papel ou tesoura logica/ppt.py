import random
import os
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033c", end='')
continua = '1'
aux_print = ['tesoura', 'pedra', 'papel']
placar = [0, 0]
while continua == '1':
    print("o placar está {} para você e {} para o computador".format(placar[0], placar[1]))
    print("(1) - Tesoura", end = "\n")
    print("(2) - Pedra", end = "\n")
    print("(3) - Papel", end = "\n")
    opcao = input("Informe uma opção acima: ")
    limpar_tela()
    try: 
        opcao = int(opcao)
        if opcao > 3 or opcao < 1: 
            print("Opção Inválida!")
        else: 
            computer = random.randint(1, 3)
            if opcao == computer:
                print(f'Empate, pois o você escolheu {aux_print[opcao - 1]} e o computador jogou {aux_print[computer - 1]}!', end="\n")
            elif (opcao == 1 and computer == 3) or (opcao == 3 and computer == 2) or (opcao == 2 and computer == 1):
                placar[0] += 1
                print(f'Parabéns, você ganhou do computador, jogando {aux_print[opcao - 1]} e o computador jogando {aux_print[computer - 1]}', end="\n")
            else:
                placar[1] += 1
                print(f'Você perdeu, pois jogou {aux_print[opcao - 1]} contra {aux_print[computer - 1]} do computador', end="\n")
            continua = input("1 - sim\nqualquer coisa - não\nDeseja continuar: ")
    except ValueError:
        print("Não é possível uma string nessa área!!!")