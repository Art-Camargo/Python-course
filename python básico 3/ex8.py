end = True
while end:
    phrase = input('Informe uma frase: ')
    phrase = phrase.upper()
    if phrase == phrase[::-1]:
        print('A palavra é palindrona!')
    else:
        print('A palavra não é palindrona!')
        end = False