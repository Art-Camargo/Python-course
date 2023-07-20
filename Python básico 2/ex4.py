TAM = 5
soma = 0
for i in range(0, TAM, 1):
    num = int(input('Informe um número: '))
    soma += num
    if i == 0:
        maior = num
    elif num > maior:
        maior = num
print(f'O maior número é igual a {maior}')
print(f'A média dos números é igual a {soma / TAM:.2f}')
print(f'A Soma dos números é igual a {soma}')

