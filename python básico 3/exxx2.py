lista = []
lista2 = []
count = 0
string = ''
for j in range(10):
    aux = input(f'Informe a letra da posição {j + 1}: ')
    while len(aux) != 1 or aux.isdigit() or '.' in aux:
        aux = input(f'Informe a letra da posição {j + 1}: ')
    aux = aux.lower()
    lista.append(aux)
    if 'a' in lista[j] or 'e' in lista[j] or 'o' in lista[j] \
        or 'i' in lista[j] or 'u' in lista[j]:
        count += 1
print(f'Quantidade de vogais na lista = {count}')
for j in range(5):
    aux2 = input('Informe uma letra: ')
    lista2.append(aux)
    if j != 0:
       if 'a' in lista2[j] or 'e' in lista2[j] or 'o' in lista2[j] \
        or 'i' in lista2[j] or 'u' in lista2[j]:
            lista2.pop() 
            
print(f'As letras consoantes digitadas em uma lista {lista2}')