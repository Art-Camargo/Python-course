import copy
pessoa = {
    'nome': 'Artur de Camargo',
    'Altura': '1.67',
    'lista1': [1, 2, 3, 4, 5, 6, 7]
}
tam = pessoa.__len__() #ou len(pessoa)
print(tam)
print(tuple(pessoa.keys()))
print(tuple(pessoa.values()))
print(tuple(pessoa.items()))
pessoa.setdefault('Idade', 20) #da um 'append' no dicionário
for keys, values in pessoa.items():
    print(f'{keys=}, {values=}')


d2 = {}
d2 = pessoa.copy() #só copia coisas imutáveis, não copia se tiver lista ou dicionários. Um está com a msm posicação da memória que outro, ou seja, eles se alteram!
d2['lista1'][2] = 10000
print(d2, pessoa)
d2 = copy.deepcopy(pessoa) #aqui, não divide a memória e copia igual
#popitem apaga a ultima chave do dicionário
#pop apaga alguma chave dita pelo user do dicionário
print(pessoa.get('nome', 'não existe')) #entra no nao existe se retornar None
#update, além de modificar a chave e o valor, adiciona, também, alguma chave com value
pessoa.update(nome='Eduarda', Altura='1.63')
