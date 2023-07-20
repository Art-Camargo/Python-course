h = 0
n = int(input('Informe um número maior que 0 e inteiro ímpar: '))
while n <= 0 or n%2 == 0:
    n = int(input('Informe um número maior que 0 e inteiro: '))
for i in range(1, n, 2):
    h += 1 / i
print(f'A soma é igual a {h:.2f}')