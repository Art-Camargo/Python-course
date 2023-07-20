phrase = 'Python é amado pela galera' \
    'Eu amo python e todos amamos!' \
    'Artur de Camargo'
print(phrase.lower().count('a'))
i = 0
while i < len(phrase):
    if phrase[i] != ' ':
        letra = phrase[i]
        qtd_letras = phrase.count(letra)
        if i == 0:
            maior = qtd_letras
            maior_l = letra
        elif qtd_letras > maior:
            maior = qtd_letras
            maior_l = letra
    print(letra, qtd_letras, end="\n\n\n")
    i += 1
print(f'A letra que mais apareceu é a: "{maior_l}", aparecendo {maior} vezes na frase!')