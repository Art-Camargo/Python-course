num = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
escolha = str(input('Informe a operação que deseja realizar\n + --> Adição\n - --> Subtração\n'))
while(escolha != '+' and escolha != '-'):
  escolha = str(input('Informe a operação que deseja realizar de forma válida\n + --> Adição\n - --> Subtração\n'))
if (escolha == '+'):
  print(num + num2)
else:
  print(num - num2) 

num3 = input('Informe um numero: ')
int_num = int(num3)
print(type(int_num), int_num)
