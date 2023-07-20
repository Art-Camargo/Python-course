def retorna_duplicada(sublista):
    duplicado = -1
    primeiro = False
    numeros_usados = set()
    for numero in sublista:
        if numero in numeros_usados and not primeiro:
            primeiro = True
            duplicado = numero
        numeros_usados.add(numero)
    return duplicado










lista_naturais = [
    [1, 2, 3, 3, 2, 1],
    [1, 4, 9, 8, 9, 4, 8],
    [1, 2, 3, 4, 3, 4],
    [1, 2, 7, 7, 5, 5]
]
for sublista in lista_naturais:
    duplicata = retorna_duplicada(sublista)
    if duplicata == -1:
        print('Não há duplicado')
    else:
        print(f'primeira Duplicata da lista {sublista} = {duplicata}')