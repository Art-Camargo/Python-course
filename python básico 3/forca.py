def draw(x):
    if x == 0:
        print('  ()\n', ' \|/\n', ' /\*')
    elif x == 1:
        print(' ()\n', '\|/\n',)
    elif x == 2:
        print(' ()\n')
jogo = input('Informe a palavra do jogo (escondido dos outos): ')
jogo = jogo.lower()
end = True
errou = 0
certos = ''
aux = 0
while end:
    tent = input('Informe uma letra: ')
    tent = tent.lower()
    while len(tent) != 1:
        tent = input('Informe uma letra: ')
        tent = tent.lower()
    if tent in jogo:
        certos += tent
    else:
        print(f'O seu erro número {aux + 1}, restam {2 - aux} chances!')
        aux += 1
    draw(aux)
    count = 0
    for i in jogo:
        if i in  certos:
            print(i, end="")
            count += 1
        else:
            print('_', end="")
    print('', end="\n\n")
    if count == len(jogo):
        end = False
        print('Você ganhou, parabens!')
    if aux == 3:
        end = False
        print('Você perdeu, pois errou 3 vezes!')