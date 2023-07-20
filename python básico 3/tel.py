ddd = input('Informe o seu ddd (ex: 54): ')
while len(ddd) != 2:
    ddd = input('Informe o seu ddd (ex: 54): ')
num = input('Informe o seu número: ')
while len(num) < 8:
    num = input('Informe o seu número: ')
if '9' not in num[0]:
    print(f'{ddd} 9 {num}')
    print(f'{ddd} 9', end="")
    for i in num:
        
else:
    print(ddd, num)
    print(ddd, '-', num)