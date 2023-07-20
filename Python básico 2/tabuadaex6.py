size = int(input('Informe até aonde vai a tabuada: '))
while size <= 0:
    size = int(input('Informe até aonde vai a tabuada: '))

num = int(input(f'Informe o número que você deseja saber a tabuada que vai do 0 até o {size}: '))
while num <= 0:
    num = int(input(f'Informe o número que você deseja saber a tabuada que vai do 0 até o {size}: '))

for i in range(0, size + 1, 1):
     print(f'{num} X {i} = {num * i}')