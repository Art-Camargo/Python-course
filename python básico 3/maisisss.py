vet = []
aluno =[]
count = 0
letras = 'ABCDE'
end = True
for i in range(30):
    vet.append(input('Informe o gabarito da questão {}: '.format(i + 1)))
    while vet[i].isdigit() or '.' in vet[i] or len(vet[i]) != 1\
        or vet[i] not in letras :
        vet.append(input(f'Informe o gabarito da questão {i + 1} de forma adequada(a, b, c, d, e): '))
        vet[i].upper()
    vet[i].upper()
while end:
    for i in range(30):
        aluno.append(input('Informe o gabarito da questão {}: '.format(i + 1)))
        while aluno[i].isdigit() or '.' in aluno[i] or len(aluno[i]) != 1\
            or aluno[i] not in letras :
            aluno.append(input(f'Informe o gabarito da questão {i + 1} de forma adequada(a, b, c, d, e): '))
            aluno[i].upper()
        aluno[i].upper()
        count += 1
    print('Esse seu aluno acertou {} questões'.format(count))
    escolha = input('Caso queira corrigir a prova de algum aluno a mais, tecle 0. Caso não, aperte qualquer tecla e de enter')
    if escolha != 0:
        end = False
    else:
        aluno.clear()
        count = 0

