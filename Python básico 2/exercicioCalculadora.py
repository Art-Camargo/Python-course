
end = False
op = '+-/*powsqrt'
while end == False:
    num = input('Informe o primeiro número: ') or 'Número 1 não informado'
    error = num
    num2 = input('Informe o segundo número: ') or 'Número 2 não informado'
    try:
        num = float(num)
        error = num2
        num2 = float(num2)
        numbers = True
    except:
        numbers = False
    if numbers == False:
        print(f'Impossível continuar, pois a opção "{error}" não é um número float!')
    elif numbers == True:
        print('* PARA multiplicação')
        print('pow PARA potenciação do primeiro elevado ao segundo')
        print('/ PARA divisão')
        print('+ PARA soma')
        print('- PARA subtração')
        pick = input('Escolha uma das opções acima: ')
        if pick == 'POW':
            pick = pick.lower()
        while pick not in op:
            pick = input(f'"{pick}" não é válido, digite uma operação válida: ')
        if pick == '+':
            print(num + num2)
        elif pick == '-':
            print(num - num2)
        elif pick == '/':
            print(num / num2)
        elif pick == 'pow':
            print(pow(num, num2))
        else:
            print(num * num2)
    end = input('Deseja realizar mais operações? Digite Sim ou Não: ')
    end = end.upper()
    if end == 'NÃO' or end == 'N' or end == 'NAO':
        print(f'Você digitou a opção {end}, portanto, até a próxima!')
        end = True
    else:
        end = False