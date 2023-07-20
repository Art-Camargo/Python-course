num = input('Enter a size number(int): ')
i = 0
j = 0
try:
    num = int(num)
    while(i < num):
        while(j <= i):
            print('*', end=" ")
            j += 1
        print('\n')
        i += 1
        j = 0
except:
    print(f'O que foi digitado: {num} não é um número inteiro!')