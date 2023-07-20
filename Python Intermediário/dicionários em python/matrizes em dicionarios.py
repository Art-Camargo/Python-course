matriz = {}
aux = 0
for i in range(3):
    for j in range(3):
        matriz.setdefault((i, j), aux) 
        aux += 1
print(matriz[(0, 0)]) #usando tupla pra índices da matriz dicionário