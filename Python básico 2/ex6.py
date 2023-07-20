count = 1
n = int(input('Informe um valor maior que 0: ')) or 'Você não digitou nada'
while n < 1:
    n = int(input('Informe um valor maior que 0: ')) or 'Você não digitou nada'
for i in range(0, n + 1, 1):
    for j in range(1, i + 1, 1):
        if i%j == 0:
            count += 1
    if count == 2:
        print(f'O número {i} é primo entre 1 e {n}!')
    count = 0     