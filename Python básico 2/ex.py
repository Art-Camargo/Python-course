"""
Fazer um programa que leia vários números (um por vez) e imprima 0(zero) 
se o número não for múltiplo de 2,3, 5 e 7. 
Imprimir 1(um) se o número for múltiplo de 2 ou 3 e 2(dois) se o número for múltiplo de 5 e 7. 
Sair do programa quando for digitado o valor -1.
"""
end = False
while end == False:
    num = input('Informe um número INTEIRO: ')
    try:
        num = int(num)
        if num%2 == 0 and num%3 == 0 and num%5 == 0 and num%7 == 0:
            print('0', end="\n\n")
        elif num%2 == 0 or num%3 == 0:
            print('1', end="\n\n")
        elif num%5 == 0 and num%7 == 0:
            print('2', end="\n\n")
        else:
            print(f'{num} não é multiplo das condições acima')
    except:
        print(f'Você digitou {num} e isso não é um número inteiro')