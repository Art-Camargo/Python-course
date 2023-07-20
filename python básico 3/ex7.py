name = input('Informe o seu nome: ')
for i in range(0, len(name), 1):
    for j in range(0, i + 1, 1):
        print(name[i], end="")
    print('', end="\n")