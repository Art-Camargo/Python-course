pessoa = {
    
}
#pessoa['Nome'] = 'Artur' também funciona
index = 'Artur'
pessoa[index] = 'Ama Carros e Inglês'
#
pessoa['altura'] = '1.65'
print(pessoa)
del pessoa['altura']

if pessoa.get('sobrenome') is None:
    print('Não existe!!')

print(4 == '4')