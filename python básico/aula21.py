#operador and e or
enter = input('Informe a suia opção: [E]: Entrar, [S]: Sair')
password = '1234'
if enter == 'E' or enter =='e':
    senha = input(f'Visto que você digitou {enter}, qual a sua senha?')
    if senha == password and type(senha) == str:
        print(f'Senha {senha} é válida!')
    else:
        print(f'a senha {senha} não é válida!')
elif enter == 'S' or enter =='s':
    print('Você saiu do sistema!')
else:
    print('Opção não válida!')