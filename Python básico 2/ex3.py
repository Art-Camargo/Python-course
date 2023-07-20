a = input( 'Informe um numero de habitantes: ')
a = int(a)
b = input('Informe um numero de habitantes um pouco maior que o primeiro: ')
b = int(b)
anos = 0
while a < b:
    a += a*0.030
    b += b*0.015
    anos += 1
print(f'Demorou {anos} anos para a cidade A ultrapassar a B em {a - b:.2f} de habitantes')