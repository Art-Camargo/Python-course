import re
#metaCHARS
# . ^ $ * + ? { } [ ] \ | ( )
# [] conjunto de chars em uma lógica OR
#| OR
#. QUALQUER CHAR, MENOS QUEBRA DE LINHA, PENSAR EM CPF!!!
# - ranges [0-9a-zA-Z]
# flags=
#em casos específicos, no caso do ., usar \ antes, para pegar o char, não o metachar

#quantificadores metachars
# * = 0 ou n
# + = 1 ou n
# ? = 1 ou 0 (if bool)
# {n}, {min, max} ELES SEMPRE VEM APÓS O CHAR, À DIREITA DO CHAR
texto = '''
    Os raios de sol dançavam na água cristalina,
    enquanto risadas ecoavam pela praia. 
    Crianças construíam castelos de areia,
    mergulhavam nas ondas e perseguia gaivotas no céu azul. 
    Casais caminhavam de mãos dadas à beira-mar, deixando pegadas na areia molhada.
    Surfistas deslizavam nas ondas, desafiando a força do oceano.
'''
texto2 = '''
    Artur, artr, artuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuur
    joooaaaaaaaaaaaaaaaaoo
'''
cpf = '055.165.260-86,05516526086'
print(re.findall(r'Crianças|Casa.s|..................', texto)) # | = or
print(re.findall(r'ARTUR', texto2, flags=re.IGNORECASE)) #funciona tipo uma lógica ou
if re.search(r'[0-9][0-9][0-9]\.[0-9][0-9][0-9]\.[0-9][0-9][0-9][-][0-9][0-9]', cpf):
    print(re.findall(r'[0-9][0-9][0-9]\.[0-9][0-9][0-9]\.[0-9][0-9][0-9][-][0-9][0-9]', cpf))
else:
    print('Cpf sem pontuação')

print(re.findall(r'artu+r', texto2, flags=re.IGNORECASE)) #pega todos os u, por tem o + à dirteita da letra
print(re.findall(r'artu*r', texto2, flags=re.IGNORECASE)) #pega todos os u, por tem o + à dirteita da letra
print(re.findall(r'jo{3}ao{1,2}', texto2, flags=re.IGNORECASE)) #pega todos os u, por tem o + à dirteita da letra


texto3 = 'João ama ser amado'
print(re.findall(r'ama[do]{0,2}', texto3))