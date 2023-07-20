#1
num = input('Informe um número intero: ') or 'Você não digitoou nada!'
try:
    num = int(num)
    if num%2 == 0:
        print(f'O número {num} é um número par!', end="\n\n\n")
    else:
        print(f'O número {num} é um número impar!', end="\n\n\n")
except:
    print(f'Você digitou "{num}", isso não é um número inteiro, pois é um {type(num)}', end="\n\n\n")


#2
hour = input('Informe a hora do dia que você toma remédio (0 - 23): ') or 'Você não digitoou nada!'
try:
    hour = float(hour)
    if hour > 23.59 or hour < 0:
        print(f'O horário {hour:.2f} não existe, apenas se você vive em alguma cidade distinta', end="\n\n\n\n")
    elif hour >= 0 and hour <= 11:
        print(f'O horário {hour:.2f} é tido como BOM DIA', end="\n\n\n\n")
    elif hour > 11 and hour <= 17:
        print(f'O horário {hour:.2f} é tido como BOA TARDE', end="\n\n\n\n")
    else:
        print(f'O horário {hour:.2f} é tido como BOA NOITE', end="\n\n\n\n")
except:
    print(f'Você digitou {hour} e isso não é um horário válido, é uma {type(hour)}', end="\n\n\n\n")

#3
name = input('Informe o seu nome: ') or 'Você não digitou nada!'
try:
    name = float(name)
    print(f'Isso não é um nome, é um número do tipo {type(name)}')
except:
    if len(name) <= 4:
        print(f'O nome {name} é muito curto')
    elif len(name) == 5:
        print(f'O nome {name} é aceitável')
    else:
        print(f'O seu nome é muito grande! {name}')

