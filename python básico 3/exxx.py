vet = []
string = []
notas = []
soma = 0
qtd = 0
for j in range(0, 4, 1):
    aux = int(input(f'Informe o valor da posição {j + 1} do vetor: '))
    vet.insert(j, aux)
print(vet[::-1])

for j in range(0, 4, 1):
    aux2 = input(f'Informe uma palavra ou letra (posição {j + 1}): ')
    aux2 = aux2.capitalize()
    string.append(aux2)
print(sorted(string))

for j in range(3):
    aux3 = float(input(f'Informe o valor da nota {j + 1}: '))
    notas.append(aux3)
    soma += notas[j]
    qtd += 1
    if j == 0:
        maior = notas[j]
    elif notas[j] > maior:
        maior = notas[j]
media = soma / qtd
for j in range(3):
    print(f'Nota {j + 1} = {notas[j]}')
    if maior == notas[j]:
        print(f'A maior nota foi a {notas[j]}, que corresponde a prova {j + 1}')
print(f'Média das notas: {media:.2f}')

