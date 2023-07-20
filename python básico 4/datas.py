data = '22/04/2005'
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
fim = data.split('/')
for i in range(3):
    if i == 1:
        if fim[i] != 0:
            print(' de', meses[fim[i]], end="")
    elif i == 2:
        print(' de', fim[i], end="")
    else:
        print(fim[i], end="")


