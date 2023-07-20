meses = [
  'Janeiro',
  'Fevereiro',
  'Março',
  'Abril',
  'Maio',
  'Junho',
  'Julho',
  'Agosto',
  'Setembro',
  'Outubro',
  'Novembro',
  'Dezembro'
]
temperatura = []
soma = 0
for i in range(12):
    aux = float(input(f'Informe a temperatura de {meses[i]}: '))
    temperatura.append(aux)
    soma += aux
print('', end="\n\n")
for i in range(12):
    print(f'O mês de {meses[i]} teve temperatura média de {temperatura[i]}')
print(f'A média total da temperatura anual: {soma/12:.2f}' )