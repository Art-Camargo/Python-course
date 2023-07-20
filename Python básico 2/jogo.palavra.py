palavra = 'perfume'
end = False
string = ''
while end == False:
    letra = input(' Informe uma letra: ') or 'Você não digitou nada!'
    while len(letra) != 1:
        letra = input(' Informe APENAS uma letra: ') or 'Você não digitou nada!' 
    if letra in palavra:
        string += letra
    for i in palavra:
        if i in string:
            print(i, end="")
        else:
            print('*', end="")
    print('', end="\n\n")
    