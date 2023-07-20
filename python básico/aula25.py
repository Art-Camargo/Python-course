# usar tipo o format, mas com %, igual à linguagem C
preco = 1000.2323123
nome = 'Artur'
resposta = '%s é o meu nome e eu pagaria nessa camisa um valor máximo de %.2f' % (nome, preco)
print(resposta)

hexa = input('Informe um valor que a converção será feita: ')
hexa = int(hexa)
print('O valor %.2f corresponde, em hexa, ao valor %.4x! ' % (hexa, hexa))