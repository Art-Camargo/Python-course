#f-string, formatação de strings em pythonzinho de cria
nome = 'Artur de Camargo'
altura = 1.67
peso = 56.6
imc = peso / pow(altura, 2)
print(nome, 'tem', altura, 'de altura,', 'pesando', peso, 'KG,', 'tendo um imc de: ', imc, sep=" ", end="\n\n")
print(f'{nome} tem {altura:.2f} metros', end="\n\n")
print(f'{nome} pesa {peso:.2f} KG', end="\n\n")
print(f'{nome} tem um IMC === {imc:.2f}')

nome2 = 'Eduarda'
altura_2 = 1.64
print(f'Nome do entrevistado: {nome2}, altura do entrevistado: {altura_2}', end="\n\n\n\n\n")