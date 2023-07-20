nome = 'Artur'
print(nome[0])
#0 ao fim
#-1 ao fim, negativo
print('v' not in nome)
print('A' in nome, end='\n\n\n\n\n\n\n')

phrase = input('Informe uma frase genérica: ')
src = input('Informe uma letra que deseja encontrar na frase: ')
if src in phrase:
    print(f'a letra "{src}" está no na frase "{phrase}"')
else:
    print(f'a letra "{src}" não está no na frase "{phrase}"')

