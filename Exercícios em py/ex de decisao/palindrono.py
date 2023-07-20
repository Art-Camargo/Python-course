frase = input('Informe uma palavra: ')
choice = frase[:: - 1]
if frase == choice:
    print('A palavra é palindrona')
else:
    print('A palavra não é palidrona')