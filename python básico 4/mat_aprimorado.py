jogo = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
def imprime_tabuleiro(jogo):
    print(f' {jogo[0][0]} | {jogo[0][1]} | {jogo[0][2]}')
    print('---/----/---')
    print(f' {jogo[1][0]} | {jogo[1][1]} | {jogo[1][2]}')
    print('---/----/---')
    print(f' {jogo[2][0]} | {jogo[2][1]} | {jogo[2][2]}')
while True:  
    conta_jogada = 0
    while True:
        imprime_tabuleiro(jogo)
        row = int(input('Informe a posição da linha que deseja jogar: '))
        if row > 3 or row < 1:
            print('Error, posição inválida')
        else:
            size = int(input('Informe a posição da coluna que deseja jogar: '))
            if size > 3 or size < 1:
                print('Error, posição inválida: ')
            elif jogo[row - 1][size - 1] == 'X' or jogo[row - 1][size - 1] == 'O':
                print('Posição inválida')
            else:
                if conta_jogada%2==0:
                    jogo[row - 1][size - 1] = 'X'
                else:
                    jogo[row - 1][size - 1] = 'O'
                conta_jogada += 1
                for i in range(3):
                    for k in range(3):
                        if i == 0:
                            if k + 2 < 3 and jogo[i][k] == jogo[i][k + 1] == jogo[i][k + 2] and jogo[i][k] != ' ':
                                print('O jogador ganhou!')
                                break
                        if k == 0:
                            if i + 2 < 3 and jogo[i][k] == jogo[i + 1][k] == jogo[i + 2][k] and jogo[i][k] != ' ':
                                print('O jogador ganhou!')
                                break
                        if i == k:
                            if i + 2 < 3 and k + 2 < 3 and jogo[i][k] == jogo[i + 1][k + 1] == jogo[i + 2][k + 2] and jogo[i][k] != ' ':
                                print('O jogador ganhou!')
                                break
                        if jogo[0][2] == jogo[1][1] == jogo[2][0] and jogo[0][2] !=' ':
                            print('O jogador ganhou!')
                            break
                if conta_jogada == 9:
                    print("Empate")
                    break
    for i in range(3):
        for k in range(3):
            jogo[i][k] = ' '
