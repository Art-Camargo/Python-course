def calcular_imposto(preco):
   return preco * 1.3

preco = 2237.34
print(f'{calcular_imposto(preco):.2f}')

calcula_imposto2 = key=lambda x: x * 1.3
#var = key=lambnda parâmetro: retorno da fução pelo parâmetro

print(calcula_imposto2(preco))



