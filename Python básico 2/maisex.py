num = int(input('Informe um valor positivo maios que 0: '))
result = 1
while num < 0:
    num = int(input('Informe um valor positivo maios que 0: '))
for i in range(num, 0, -1):
    result = result * i
print(f'{num}! = {result}')