from pprint import pprint

lista_inteiros = [
    {'numero': [5, 8, 1, 0, 9, -2, -1, 0]},
    {'numero': [4, 3, -1, 0, 0, 7, 11, 10]}
]

for dicionario in lista_inteiros:
    dicionario['numero'].sort()
pprint(lista_inteiros)
        