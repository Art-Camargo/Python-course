jogo = 'Ariana'
jogo = jogo.upper()
user = [
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', '']
]
game = False
for i in range(len(jogo)):
    for j in range(len(jogo)):
        aux = input(f'Informe uma letra {i + 1}X{j + 1}: ')
        while aux.isdigit() or len(aux) != 1:
            aux = input('Informe uma letra {}: '.format(i + 1, j + 1))
        user[i][j] += aux.upper()
for i in range(len(jogo)):
    for j in range(len(jogo)):
        if i == 0:
            if user[i][j] == 'A' and user[i][j + 1] == 'R' and user[i][j + 2] == 'I'\
            and user[i][j + 3] == 'A' and user[i][j + 4] == 'N' and user[i][j + 5] == 'A':
                print(f'Palavra encontrada na posicão ({i}, {j}, {i}, {j + 1}, {i}, {j + 2}, {i}, {j + 3}, {i}, {j + 4}, {i}, {j + 5})')        
                game = True
        if j == 0:
            if user[i][j] == 'A' and user[i + 1][j] == 'R' and user[i + 2][j] == 'I'\
            and user[i + 3][j] == 'A' and user[i + 4][j] == 'N' and user[i + 5][j] == 'A':  
                print(f'Palavra encontrada na posicão ({i}, {j}, {i + 1}, {j}, {i + 2}, {j}, {i + 3}, {j}, {i + 4}, {j}, {i + 5}, {j})')     
                game = True
        if j == i:
            if user[i][j] == 'A' and user[i + 1][j + 1] == 'R' and user[i + 2][j + 2] == 'I'\
            and user[i + 3][j + 3] == 'A' and user[i + 4][j + 4] == 'N' and user[i + 5][j + 5] == 'A':       
                print('A palavra {} está na diagonal principal! '.format(jogo)) 
                game = True
for i in range(len(jogo)):
    if user[i][(len(jogo) - 1) - i] == 'A' and user[i][(len(jogo) - 2) - i] == 'R' and\
    user[i][(len(jogo) - 3) - i] == 'I' and user[i][(len(jogo) - 4) - i] == 'A'    and\
    user[i][(len(jogo) - 5) - i] == 'N'  and user[i][(len(jogo) - 1) - i] == 'A':
        print('A palavra {} está na diagonal secundária! '.format(jogo))
        game = True
if not game:
    print('Palavra {} não encontrada'.format(jogo))