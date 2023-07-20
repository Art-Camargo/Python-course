# fluxo do interpretador
condicao = True
if condicao:
  print(f'Condição está em {condicao}', end="\n\n")
else:
  print(f'A condição está em {condicao}', end="\n\n")

string = 'Eu amo a minha namorada chamada {mor}, que tem {id} anos de idade'
formata = string.format(mor = 'Eduarda', id = 17)
print(formata, end="\n\n\n")