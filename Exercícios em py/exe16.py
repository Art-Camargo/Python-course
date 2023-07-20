metros = int(input('Informe os metros quadrados: '))
if metros % 54 == 0:
  qtd_latas = metros / 54
else:
  qtd_latas = metros // 54
  qtd_latas += 1
valor = qtd_latas * 80
print(f'Quantidade de latas totais: {qtd_latas}', end="\n\n")
print(f'Valor total da compra: {valor}', end="\n\n")
print(f'Metros totais pintados: {metros}')