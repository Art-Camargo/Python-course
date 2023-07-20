num = int(input('Informe um valor: '))
num2 = int(input('Informe outro valor maior: '))
while num2 <= num:
    num2 = int(input('Informe outro valor maior: '))
soma = 0
for i in range(num, num2 + 1, 1):
    print(i)
    soma += i
print(f'Soma == {soma}')