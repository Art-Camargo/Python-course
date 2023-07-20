#print(list(range(10))) #faz o for e adiciona um a um na sting
import random 
from pprint import pprint
lista = []
for numero in range(10):
    lista.append(numero)
#print(lista) #igual a de cima

lista2 = [
    random.randint(0, 9) * 2 #o numero que vai adicionar antes do for * 10
    for _ in range(10)
]
print(lista, lista2) #à esqueda do for, eu falo o que quero incluir na lista

produtos = [
    {'nome': 'p1', 'preco': 120},
    {'nome': 'p2', 'preco': 110},
    {'nome': 'p3', 'preco': 130}
]

copia_precos = [
    {**produto, 'preco': produto['preco'] * 1.1} #tudo à esquerda do for
    if produto['preco'] >= 120 else {**produto}
    for produto in produtos
    if produto['preco'] <= 120
]
pprint(copia_precos, sort_dicts=True)
#lista3 = [_ for _ in range(10) if _ >= 3]
#print(lista3)
#esqueda do for mapeamento, direita é filtro
