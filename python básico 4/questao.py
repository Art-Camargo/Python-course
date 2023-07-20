sistems = [
  'Windows       ',
  'Unix          ',
  'Linux         ',
  'Netware       ',
  'Mac OS        ',
  'Outros        '
]
count = [0, 0, 0, 0, 0, 0]
qtd = 0
print(count)
end = True
while end:
    for i in range(len(sistems)):
        print('{} - {}'.format(i + 1, sistems[i]))
    op = int(input('Informe uma opção (0 == fim): '))
    while op > 6 or op < 0:
        op = int(input('Informe uma opção correta (0 == fim): '))
    if op == 0:
        end = False
    else:
        count[op - 1] += 1
        qtd += 1
print('Sistema operacional     votos      %')
print('-------------------     -----      -')
for i in range(len(sistems)):
    print('{} - {}'.format(i + 1, sistems[i]), '      ', count[i], '      ', f'{(count[i] * 100) / qtd:.2f}')
print(f'TOTAL DE VOTOS = {qtd}')