string = 'abcd'
lista = ['Artur', 123, 123]
del lista[2]
print(lista)
print(lista[0].upper())
lista.append('Artur de Camargo')
lista.append('aa')
lista.append('Abb')
print(lista.pop())

lista2 = ['A', 'N', 'Ã', 'O']
lista3 = lista2 + lista
print(lista3)
lista3 = lista3.insert(0, 'AMO A MINHA MULHER')
print(lista3)