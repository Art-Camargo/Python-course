par = []
impar = []
vet = []
for i in range(20):
    aux = int(input('Informe um número: '))
    vet.append(aux)
for i in range(20):
    if vet[i]%2 == 0:
        par.append(vet[i])
    else:
        impar.append(vet[i])
print('Vetor completo: ', vet)
print('Vetor par completo: ', par)
print('Vetor ímpar completo: ', impar)
