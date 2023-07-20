import os
def printa_tabuleiro(game_cmd):
    for i in range(3):
        for j in range(3):
            print(f'|{game_cmd[i][j]}|', end='')
        print('\n')

def posicao_tabuleiro(game_cmd, aux):
    posicao = input('Informe a ' + aux + ' que deseja jogar: ')
    while posicao != '1' and posicao != '2' and posicao != '3':
        posicao = input('Error. Informe a ' + aux + ' que deseja jogar: ')
    return posicao

def troca_jogador(jogador):
    if jogador == 'X':
        return 'O'
    else:
        return 'X'

def ganhou_diagonais(game_cmd):
    for i in range(3):
        for j in range (3):
            if i == j and i == 0:
                if (game_cmd[i][j] == 'X' and game_cmd[i + 1][j + 1] == 'X' and game_cmd[i + 2][j + 2] == 'X') \
                or (game_cmd[i][j] == 'O' and game_cmd[i + 1][j + 1] == 'O' and game_cmd[i + 2][j + 2] == 'O'):
                    print(f'O jogador {game_cmd[i][j]} ganhor')
                    return True
            if j == 2 and i == 0:
                if (game_cmd[i][j] == 'X' and game_cmd[i + 1][j - 1] == 'X' and game_cmd[i + 2][j - 2] == 'X') \
                or (game_cmd[i][j] == 'O' and game_cmd[i + 1][j - 1] == 'O' and game_cmd[i + 2][j - 2] == 'O'):
                    print(f'O jogador {game_cmd[i][j]} ganhor')
                    return True
    return False

def ganhou_linhas_colunas(game_cmd):
    for i in range(3):
        for j in range (3):
            if i == 0:
                if (game_cmd[i][j] == 'X' and game_cmd[i + 1][j] == 'X' and game_cmd[i + 2][j] == 'X') \
                or (game_cmd[i][j] == 'O' and game_cmd[i + 1][j] == 'O' and game_cmd[i + 2][j] == 'O'):
                    print(f'O jogador {game_cmd[i][j]} ganhor')
                    return True
            if j == 0:
                if (game_cmd[i][j] == 'X' and game_cmd[i][j + 1] == 'X' and game_cmd[i][j + 2] == 'X') \
                or (game_cmd[i][j] == 'O' and game_cmd[i][j + 1] == 'O' and game_cmd[i][j + 2] == 'O'):
                    print(f'O jogador {game_cmd[i][j]} ganhor')
                    return True

continua = True
while continua:
    end = False
    game_cmd = [[' ' for _ in range(3)] for _ in range(3)] #primeiro for é as diagonais, o segundo é as linhas
    jogador = 'X'
    while not end:
        printa_tabuleiro(game_cmd)
        linha = int(posicao_tabuleiro(game_cmd, 'linha')) - 1
        coluna = int(posicao_tabuleiro(game_cmd, 'coluna')) - 1
        os.system("cls")
        if game_cmd[linha][coluna] != ' ':
            print(f'Posição {linha=}, {coluna=} é inválida, pois já foi jogada.')
        else:
            game_cmd[linha][coluna].replace(' ', jogador)
            if ganhou_diagonais(game_cmd) or ganhou_linhas_colunas(game_cmd):
                end = True
            else:
                
    
            
        


