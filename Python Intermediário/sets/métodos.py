s = set()
s.add('Luiz')
s.add('Artur')
#s.update('Ola') #assim, manda index a index
s.update(('Artur', 123)) #com iterável, pra ir inteiro
s.discard('Artur')
print(s)
s.clear()

#operadores úteis:
#uniao | (ou .union())
#intersecção & (ou .intersection())
#diferença - (ou .difference)
#diferença simétrica ^ (ou .symmetric_difference)
s1 = {1, 2, 3}
s2 = {2, 3, 4}
#PRINCIPAL CARACTERISTICA, NÃO SALVA VALROES JA SALVOS

