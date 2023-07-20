def recebe_num():
    numero = input('Informe um número: ')
    if  numero.isdigit():
        return numero
    return None

lista_numeros = []

continua = True
while continua:
    num = recebe_num()
    if num is not None:
        lista_numeros.append(int(num))
    opcao = input('se quiser continuar, tecle algo diferente de 0: ')
    if opcao == '0':
        continua = False
even_numbers = list(filter(lambda x: int(x) % 2 == 0, lista_numeros))
odd_numbers = list(filter(lambda x: int(x) % 2 != 0, lista_numeros))
print(f'Números pares = {even_numbers}.\nNumeros ímpares = {odd_numbers}')