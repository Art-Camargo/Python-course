import os

def printa_invalido(cpf_teste):
    print(f'O cpf {cpf_teste} não é válido. Por favor, informe outro cpf')

def valida_cpf(cpf_teste):
    cpf_lista = list(cpf_teste)  # Converter a string em uma lista de caracteres
    acumulador = 0
    j = 10
    for i in range(0, 9):
        try:
            cpf_lista[i] = int(cpf_lista[i])
            acumulador += cpf_lista[i] * j
            j -= 1
        except:
            return False
    if (acumulador // 11) < 2 and int(cpf_lista[9]) != 0 or acumulador // 11 >= 2 and int(cpf_lista[9]) != 11 - acumulador % 11:
        return False
    j = 11
    acumulador = 0
    for i in range(0, 10):
        try:
            cpf_lista[i] = int(cpf_lista[i])
            acumulador += cpf_lista[i] * j
            j -= 1
        except:
            return False
    if acumulador // 11 < 2 and int(cpf_lista[10]) != 0 or acumulador // 11 >= 2 and int(cpf_lista[10]) != 11 - acumulador % 11:
        return False
    else:
        return True


invalido = True
while invalido:
    cpf_teste = input('Informe o seu cpf: ')
    os.system("cls")
    sequencial_input = (cpf_teste == cpf_teste[0] * 11)
    if len(cpf_teste) == 11 and not sequencial_input:
        if valida_cpf(cpf_teste):
            print(f'O cpf {cpf_teste} é um cpf válido!')
            invalido = False
        else:
            printa_invalido(cpf_teste)
    else:
        printa_invalido(cpf_teste)
