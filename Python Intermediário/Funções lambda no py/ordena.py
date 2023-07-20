
def exibe_lista(lista_ordenada):
    for item in lista_ordenada:
        print(item)
    print()




lista_nomes = [ 
    {'nome': 'Artur', 'sobrenome': 'Camargo'},
    {'nome': 'Thiago', 'sobrenome': 'José'},
    {'nome': 'Amara', 'sobrenome': 'Josué'},
    {'nome': 'Diego', 'sobrenome': 'Valter'},
]
ordena_nome = sorted(lista_nomes, key=lambda nomes: nomes['nome'])
ordena_sobrenome = sorted(lista_nomes, key=lambda nomes: nomes['sobrenome'])
exibe_lista(ordena_sobrenome)
exibe_lista(ordena_nome)