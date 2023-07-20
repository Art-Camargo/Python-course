num = range(0, 200, 2)
summ = 0
for i in num:
    summ += i
print(summ)
size = 7
for i in range(0, size, 1):
    for j in range(0, size, 1):
        print(f'Coluna {j + 1} e linha {i + 1}')