saltos = [
      'Primeiro salto',
      'Segundo salto',
      'Terceiro salto',
      'Quarto salto',
      'Quinto salto'
]
distancias = []
aux = 0.0
name = input('informe o seu nome: ')
while name.isdigit() or '.' in name:
    name = input('informe o seu nome: ')
for i in range(len(saltos)):
    distancias.append(float(input('Informe a distância do salto {}'.format(i + 1))))
    aux += distancias[i]
print(f'\n\nAtleta: {name}')
for i in range(len(distancias)):
    print('{}: {:.2f}m'.format(saltos[i], distancias[i]))
print('Media dos saltos: {:.2f}'.format(aux / len(distancias)))