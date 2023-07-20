respostas = 'abcdeABCDE'
alunos = input('Informe quantas provas você irá corrigir: ')
while not alunos.isdigit():
    alunos = input('Informe quantas provas você irá corrigir: ')
names = []
alunos = int(alunos)
for i in range(alunos):
    names.append(input('Informe o nome do aluno {}: '.format(i + 1)))
    while names[i].isdigit() or '.' in names:
        names.pop()
        names.append(input('Informe o nome do aluno {}: '.format(i + 1)))
qtd = input('Informe quantas questões a sua prova possui: ')
while not qtd.isdigit():
    qtd = input('Informe quantas questões a sua prova possui: ')
qtd = int(qtd)
gabarito = []
resp_alunos = []
for i in range(qtd):
    gabarito.append(input('Informe a resposta da questão {} (abcde): '.format(i + 1)))
    while gabarito[i] not in respostas:
        gabarito.pop()
        gabarito.append(input('Informe a resposta da questão {} (abcde): '.format(i + 1)))
for i in range(alunos):
    count = 0
    resp_alunos.clear()
    for j in range(qtd):
        resp_alunos.append(input('Questão {} do aluno(a) {}: '.format(j + 1, names[i])))
        while resp_alunos[j] not in respostas:
            resp_alunos.pop()
            resp_alunos.append(input('Questão {} do aluno(a) {}: '.format(j + 1, names[i])))
        if resp_alunos[j] == gabarito[j]:
            count += 1
    print(f'O aluno {names[i]} acertou {count} questões de um total de {qtd}')