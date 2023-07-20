def mostra_keyword(*args, **kwargs): #usar um não nomeado, normalmente para dicionários

    for key, value in kwargs.items():
        print(key, value)



pessoa = {
    'nome': 'Artur',
    'sobrenome': 'Camargo'
}
(chave, key), (chave2, key2) = pessoa.items()
print(f'{chave}: {key}\n{chave2}: {key2}')


dados_pessoa = {
    'Idade': 20,
    'Altura': 1.67
}

pessoa_completa = {**pessoa, **dados_pessoa} #desempacota os dicionários em outro
mostra_keyword(**pessoa_completa)




argumentos = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4 
}
mostra_keyword(**argumentos)