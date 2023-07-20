lista = [200, 299, 399, 499, 599, 699, 799, 899, 999]
count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
end = True
while end:
    salario = 0
    vendas = float(input('Informe o seu total de vendas: (0 para fim): '))
    if vendas == 0:
        end = False
    else:
        salario += 200 + (0.09 * vendas)
        for i in range(len(lista) - 1):
            if salario > lista[i] and salario < lista[i + 1]:
                count[i] += 1
            elif i == len(lista) - 1:
                if salario > 1000:
                    count[i] += 1
for i in range(len(lista) - 1):
    print(lista[i], '-', lista[i + 1], count[i])
