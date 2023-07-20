#bubble sort recursivo em python
def BubbleSortRecursivo(vetor, index):
    if index < len(vetor) - 1:
        if vetor[index] > vetor[index + 1]:
            aux = vetor[index]
            vetor[index] = vetor[index + 1]
            vetor[index + 1] = aux
            BubbleSortRecursivo(vetor, 0)
        else:
            BubbleSortRecursivo(vetor, index + 1)
    
        
index = 0
vetor = [2, 5, 1, 0, 7, 10, 2, 69, 1, 0, 0, 1]
BubbleSortRecursivo(vetor, index)
print(vetor)