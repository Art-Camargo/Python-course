import os
import copy
def valida_digitos(cpf, limitador):
    soma = 0
    for numero in cpf:
        if limitador >= 2:
            soma += limitador * int(numero)
        limitador -= 1
    resto = soma % 11
    if resto < 2:
        if int(cpf[limitador - 1]) != 0:
            return False
    elif 11 - resto != int(cpf[limitador - 1]):
        return False
    return True

def cadastra_key(database_cliente):
    valido = False
    while not valido:
        cpf = input('Informe o seu CPF (apenas números): ')
        os.system("cls")
        if not cpf.isdigit() or len(cpf) != 11:
            print('ERRO. Digite novamente o CPF')
        elif valida_digitos(cpf, 10) and valida_digitos(cpf, 11) and cpf not in database_cliente:
            database_cliente.setdefault(cpf, {
                'Nome': '',
                'Idade': ''
            })
            valido = True
        else:
            print(f'CPF {cpf} é inválido para o módulo 11 ou já está no nosso dicionário!')

def cadastra_user(database_cliente, user):
    str_valido = False
    while not str_valido:
        name = input('Informe o seu nome: ')
        if name:
            str_valido = True
            database_cliente[user]['Nome'] = name
        else:
            print('Nome inválido')
    str_valido = False
    while not str_valido:
        idade = input('Informe a sua idade: ')
        if idade.isdigit():
            if int(idade) > 0:
                str_valido = True
                database_cliente[user]['Idade'] = idade
            else:
                print('Idade inválida')
        else:
            print('Idade inválida')

database_cliente = {}
continua = True

while continua:
    cadastra_key(database_cliente)
    user = list(database_cliente.keys())[-1]
    cadastra_user(database_cliente, user)
    if len(database_cliente) == 3:
        continua = False
menores_de_18 = {}
novo = copy.deepcopy(database_cliente)
for item in novo.keys():
    if int(novo[item]['Idade']) < 18:
        menores_de_18[item] = copy.deepcopy(database_cliente[item]) 
        del database_cliente[item]
os.system("cls")
print(menores_de_18)
print(database_cliente)