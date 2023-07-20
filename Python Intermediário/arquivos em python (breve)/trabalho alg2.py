import os
import datetime
def menu():
    valido = False
    while not valido:
        print('1 - Cadastrar cliente\n2 - Listar cliente por data Informada')
        print('3 - Listar quantidade de clientes por bairro\n4 - Listar cliente com maior valor de compra')
        print('5 - Fim')
        try:
            opcao = int(input('Informe uma opção acima: '))
            os.system("cls")
            if int(opcao) > 5 or int(opcao) < 1:
                print('Inválido. Digite novamente')
            else:
                valido = True
        except:
            os.system("cls")
            print('ERROR. Enter a number', end="\n\n")
    return opcao

def valida_key(cpf_aux, limitador):
    acumulador_digitos = 0
    for digitos in cpf_aux:
        if limitador >= 2:
            acumulador_digitos += limitador * int(digitos)
        limitador -= 1
    if acumulador_digitos % 11 < 2 and int(cpf_aux[limitador - 1]) != 0:
        return False
    elif acumulador_digitos >= 2 and int(cpf_aux[limitador - 1]) != (11 - (acumulador_digitos %11)):
        return False
    return True

def valida_iguais(cpf_aux):
    repetidos = set()
    for numero in cpf_aux:
        if numero not in repetidos:
            repetidos.add(numero)
    if len(repetidos) == 1:
        return False
    return True

def cadastra_key():
    invalido = True
    while invalido:
        cpf_aux = input('Informe o seu cpf: ')
        if cpf_aux.isdigit() and len(cpf_aux) == 11:
            if valida_key(cpf_aux, 10) and valida_key(cpf_aux, 11) and valida_iguais(cpf_aux):
                invalido = False
                try:
                    with open('Clientes.txt', 'r') as arquivo:
                        for linha in arquivo.readlines():
                            if cpf_aux in linha:
                                invalido = True
                        if invalido:
                            print('Esse cpf já está cadastrado no nosso sistema')
                except:
                    print('Arquivo não abriu, pode ser um erro')
            else:
                print(f'Cpf inválido!')
    return cpf_aux

def valida_nomes(nomes):
    if not nomes or nomes[0].isdigit() or ';' in nomes:
        print('Não é permitido esáços em branco.\nNão é permitodo número no char inicial\n')
        print('Não é permitido ; nos inputs')
        return False
    return True

def cadastra_value(string_print):
    nome = input(f'Informe o seu {string_print}: ')
    while not valida_nomes(nome):
        nome = input(f'Informe o seu {string_print}: ')
    return nome.capitalize()

def valida_valor():
    mantem = True
    while mantem:
        value = input('Informe o seu valor acumulado: ')
        try:
            value = float(value)
            if value >= 0.0:
                return value
            else:
                print('Valores menores que 0.0 são desconsiderados')
        except:
            print('Apenas valores válidos')
    return value

def valida_data(data_atual, *data):
    if int(data[2]) <= 0 or (int(data[1]) > 12 or int(data[1]) < 1):
        return False 
    if int(data[1]) == 2: #mes
        if int(data[0]) % 400 == 0 or (int(data[0]) % 4 == 0 and int(data[0]) % 100 != 0): #ano bissexto
            if int(data[2]) > 29:
                return False
        else:
            if int(data[2]) > 28:
                return False
    elif int(data[1]) == 4 or int(data[1]) == 6 or int(data[1]) == 9 or int(data[1]) == 11:
        if int(data[2]) > 30:
            return False
    elif int(data[1]) == 1 or int(data[1]) == 3 or int(data[1]) == 5 or int(data[1]) == 7 \
        or int(data[1]) == 8 or int(data[1]) == 10 or int(data[1]) == 12:
        if int(data[2]) > 31:
            return False
    data = datetime.date(int(data[0]), int(data[1]), int(data[2]))
    if data > data_atual:
        return False
    return True

def cadastra_data():
    data_atual = datetime.date.today() #(YYYY-MM-DD) do dia atual
    data_valida = False
    while not data_valida:
        data = input('Informe a sua data de nascimento(dd/mm/yyyy): ')
        if len(data) != 10 or '/' not in data or data.find('/') == data.rfind('/'):
            print('Data com algum problema. Tente usar dd/mm/yyyy')
        else:
            try:
                dia, mes, ano = data.split('/')
                if (len(dia) == 2 and len(mes) == 2 and len(ano) == 4) \
                    and (dia.isdigit() and mes.isdigit() and ano.isdigit()):
                    if valida_data(data_atual, ano, mes, dia):
                        data_valida = True
                    else:
                        print(f'Data {data} é inválida')
            except:
                print('Erro de informação via teclado')
    return data

def busca_data_arquivo(data_buscas):
    achou = False
    try:
        with open('Clientes.txt', 'r') as arq:
            for linha in arq.readlines():
                sublinha = linha.split(';')
                for cadastro_separado in sublinha:
                    if data_busca == cadastro_separado:
                        print(f'{sublinha[0]}, {sublinha[1]}. Cliente que nasceu na data informada para busca')
                        achou = True
    except:
        achou = True
        print('Ainda não há um arquivo no sistema ou o arquivo está aberto em tempo de execução do programa')
    return achou

def busca_bairro(bairro_busca):
    counter = 0
    achou_bairro = False
    try:
        with open('Clientes.txt', 'r') as arquiv:
            for line in arquiv.readlines():
                line_split = line.split(';')
                if bairro_busca == line_split[3]:
                    counter += 1
                    achou_bairro = True
                    print(f'Morador do bairro {bairro_busca}: {line_split[1]}, {line_split[0]}')
    except:
        achou_bairro = True
        print('Error. File not found')
    print(f'Há um total de {counter} moradores nesse bairro')
    return achou_bairro

def printa_maior_comprador():
    max = -1.0
    try:
        with open('Clientes.txt', 'r') as arqv:
            for file_line in arqv.readlines():
                dividir = file_line.split(';')
                if float(dividir[5]) > max:
                    max = float(dividir[5])
        with open('Clientes.txt', 'r') as arqv:
            for file_line in arqv.readlines():
                dividir = file_line.split(';')
                if max == float(dividir[5]):
                    print(f'O cliente {dividir[1]} tem o maior valor acumulado em compras, sendo igual a {max:.4f}')
    except:
        print('Error. File not found')

continua = True
while continua:
    operacao_menu = menu()
    os.system("cls")
    if operacao_menu == 1:
        cpf = cadastra_key() 
        name = cadastra_value('nome') #nome 
        addrs = cadastra_value('endereço (rua e número, se houver número)')  #endereço
        bairro = cadastra_value('Bairro') 
        valor = valida_valor() 
        data_cliente = str(cadastra_data())
        with open('Clientes.txt', 'a+') as file:
            file.write(f'{cpf};{name};{addrs};{bairro};{data_cliente};{valor:.3f}\n')
    elif operacao_menu == 2:
        data_busca = cadastra_data()
        encontrou = busca_data_arquivo(data_busca)
        if not encontrou:
            print('Não há moradores cadastrados que nasceram no dia {}'.format(data_busca))
    elif operacao_menu == 3:
        bairro_busca = cadastra_value('bairro')
        encontrou_bairro = busca_bairro(bairro_busca)
        if not encontrou_bairro:
            print('Não há moradores cadastrados no bairro {}'.format(bairro_busca))
    elif operacao_menu == 4:
        printa_maior_comprador()
    else:
        continua = False
        print('program has finished. See you, take care :)')







