end = False
aux = 0
while end == False:
    num = int(input('Informe um número positivo: '))
    if num <= 0:
        end = True
    else:
        if aux == 0:
            maior = num
            menor = num
            aux += 1
        elif num > maior:
            maior = num
        elif num < menor:
            menor = num

print(f'O maior número é igual a {maior:.2f}')
print(f'O maior número é igual a {menor:.2f}')