import os
def respostas(perguntas, i):
    
    print('Pergunta: {}'.format(perguntas[i]['Pergunta']))
    for j in range(4):
        print(f'{j}) ', perguntas[i]['Opções'][j])
    op = input('Escolha uma opção acima: ')
    while op != '0' and  op != '1' and  op != '2' and  op != '3': 
        op = input('Escolha uma opção acima: ')
    os.system("cls")
    if perguntas[i]['Opções'][int(op)] == int(perguntas[i]['Resposta']): 
        print('VOCÊ ACERTOU!!')
        return 1
    else:
        print('Voce ERROU!!')
        return 0



count = 0
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2? ',
        'Opções': [1, 2, 3, 4],
        'Resposta': '4',    
    },

    {
        'Pergunta': 'Quanto é 5**3? ',
        'Opções': [8, 25, 125, 75],
        'Resposta': '125',
    },

    {
        'Pergunta': 'Quanto é 10 // 5? ',
        'Opções': [10, 5, 4, 2],
        'Resposta': '2',
    }
]
for i in range(3):
    count += respostas(perguntas, i)
print(f'Você acertou {count} testes')