nota1 = input('Informe a sua primeira nota: ')
nota1 = float(nota1)
nota2 = input('Informe a sua segunda nota: ')
nota2 = float(nota2)
nota3 = input('Informe a sua terceira nota: ')
nota3 = float(nota3)
media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f'Com a nota {media:.2f}, você foi aprovado!')
elif media < 7 and media > 0:
    print(f'Com a nota {media:.2f}, você foi reprovado!')
else:
    print(f'Com a nota {media:.2f}, você foi reprovado com distinção!')