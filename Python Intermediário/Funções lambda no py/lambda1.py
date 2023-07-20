from pprint import pprint

def printa_lista(lista_dic):
    for index in lista_dic:
        for key, value in index.items():
            print(f'{key}: {value}. ', end =" ")
        print()
        


lista = [2, 4, 4, 1, 0, 1,]
lista.sort() #bubblesort na lista
lista.sort(reverse=True) #bubblesort inverso?
print(lista)
lista_dic = [
    {
     'nome': 'Valentina',
     'Sobrenome': 'Camargo'
    },
    {
     'nome': 'Jurema',
     'Sobrenome': 'Maria'
    },
    {
     'nome': 'Artur',
     'Sobrenome': 'Camargo'
    },
    {
     'nome': 'Eduarda',
     'Sobrenome': 'Valter'
    }
]
 #sem lambd

lista_dic = sorted(lista_dic, key=lambda ordenakey: ordenakey['nome'])
printa_lista(lista_dic)
 #ordena por lambda

