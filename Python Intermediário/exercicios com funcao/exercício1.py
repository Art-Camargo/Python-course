def sequencia(numero, n):
    if n <= numero:
        for i in range(n):
            print(n, end="")
        print('', end="\n")
        sequencia(numero, n + 1)


numero = 9
sequencia(numero, 1)