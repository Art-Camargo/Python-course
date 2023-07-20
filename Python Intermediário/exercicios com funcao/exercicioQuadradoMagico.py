import numpy as np

def criar_quadrado_magico(n):
    matriz = np.zeros((n, n), dtype=int)
    i = n // 2
    j = n - 1
    count = 1

    while count <= n * n:
        if i == -1 and j == n:
            j = n - 2
            i = 0
        else:
            if j == n:
                j = 0
            if i < 0:
                i = n - 1

        if matriz[int(i)][int(j)]:
            j = j - 2
            i = i + 1
            continue
        else:
            matriz[int(i)][int(j)] = count
            count += 1

        j = j + 1
        i = i - 1

    return matriz

# Cria um quadrado mágico de ordem 3
quadrado_magico = criar_quadrado_magico(3)
print('Quadrado mágico:')
print(quadrado_magico)
