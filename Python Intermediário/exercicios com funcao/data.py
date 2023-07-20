import os
def valida_data(data):
    if not data[0].isdigit() or not data[1].isdigit() or not data[2].isdigit():
        return False
    else:
        if int(data[1]) > 12 or int(data[1]) < 1 or int(data[0]) <= 0:
            return False
        elif int(data[2]) <= 0:
            return False
        elif int(data[1]) == 1 or int(data[1]) == 3 or int(data[1]) == 5 or\
        int(data[1]) == 7 or int(data[1]) == 8 or int(data[1]) == 10 or int(data[1]) == 12:
            if int(data[0]) > 31:
                return False
        elif int(data[1]) == 4 or int(data[1]) == 6 or int(data[1]) == 9 or\
        int(data[1]) == 9:
            if int(data[0])  > 30:
                return False
        else:
            if int(data[2]) % 400 == 0 or (int(data[2]) % 4 == 0 and int(data[2]) %100 != 0):
                if int(data[0]) > 29:
                    return False
            elif int(data[0]) > 28:
                return False
    return True                            

def printa_data(meses, data):
    mes = data[1]
    print(f'Sua data: {data[0]} de {meses[int(mes) - 1]} de {data[2]}')

continua = True
meses = [
    'Janeiro', 'Fevereiro', 'Março',
    'Abril', 'Maio', 'Junho', 'Julho',
    'Agosto', 'Setembro', 'Outubro', 
    'Novembro', 'Dezembro'
]
while continua:
    data = input('Informe uma data (dd/mm/yyyy): ')
    os.system("cls")
    if len(data) != 10:
        print('Data com tamanho inválido. Lembre-se de usar /')
    else:
        try:   
            data = data.split('/')
            if valida_data(data):
                printa_data(meses, data)
                opcao = input('1 - Sim\nQualquer tecla - Não\nDeseja continuar? ')
                os.system("cls")
                if opcao != '1':
                    continua = False
            else:
                print(f'Data {data} Inválida')
        except:
            print('Error! Something went wrong')