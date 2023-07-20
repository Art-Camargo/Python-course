import re
continua = True
while continua:
    cpf = input('Informe o seu cpf: ')
    if re.search(r'[0-9][0-9][0-9]\.[0-9][0-9][0-9]\.[0-9][0-9][0-9]-[0-9][0-9]', cpf):
        print(f'cpf válido com pontos {cpf}')
        cpf = re.sub(r'\.|-', '', cpf)
        continua = False
    elif cpf.isdigit() and len(cpf) == 11:
        print(f'cpf válido sem pontos {cpf}')
        continua = False
    else:
        print(f'{cpf} é um cpf inválido')
print(cpf)