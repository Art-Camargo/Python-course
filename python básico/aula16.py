#if, else, elif
entrada = input('Você quer entrar, sair ou recarregar a página? ', end="\n\n")

if entrada == 'entrar':
  print(f'Você entrou no servidor, pois escolheu a opção "{entrada}" ;) ', end="\n\n")
elif entrada == 'sair':
  print(f'Você saiu do serviros, pois escolheu a opção "{entrada}" ;)', end="\n\n")
elif entrada == 'recarregar':
  print(f'Você escolheu recarregar a página do servidor, pois escolheu a opção "{entrada}" ;', end="\n\n")
else:
  print('Opção não é valida!')
