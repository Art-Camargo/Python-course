# try
#except
Numero = input('Informe um numero: ')
if Numero.isdigit():
    Numero = float(Numero)
    print(f'O dobro de {Numero:.2f} é {Numero * 2:.2f}', end="\n\n\n\n\n")
else:
    print('Isso não é um número!', end="\n\n\n\n\n")

num = input('Informe um número: ')
try: 
    print(type(num))
    num = float(num)
    print(f'O dobro do seu número === {num * 2:.2f} ')
except:
    print('Isso não é um número!')