size = int(input('Informe um tamanho: '))
aux = size // 2 
aux2 = size // 2
for i in range(size):
    for j in range(size):
        if i <= size // 2:
            if j >= i and j <= (size - 1) - i:
                print('  ', end="")
            else:
                print('* ', end="")
        else:
            if j == 0:
                aux += 1
                aux2 -= 1
            if j >= aux2 and j <= aux:
                print('  ', end="")
            else:
                print('* ', end="")
    print('', end="\n")