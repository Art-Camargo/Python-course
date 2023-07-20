#programa para validar data em python
import os
def valida_data(data_original):
    meses30 = [4, 6, 9, 11]
    meses31 = [1, 3, 5, 7, 8, 10, 12]
    try:
        dia, mes, ano = map(int, data_original)
        if mes < 1 or ano < 1 or dia < 1 or mes > 12:
            return False
        if mes in meses30:
            if dia > 30:
                return False
            else:
                return True
        elif mes in meses31:
            if dia > 31:
                return False
            else: 
                return True
        else:
            if ano %400 == 0 and ano % 4 == 0 and ano % 100 != 0:
                if dia > 29:
                    return False
                else:
                    return True
            else:
                if dia > 28:
                  return False
                else:
                    return True
    except:
        print("\nErro de execução")
        return True
continua = True
while continua:
    data = input("Informe uma data dd/mm/yyyy: ")
    os.system('cls' or 'clear') or print("\n" * 100)
    conta_barra = data.count("/")
    if len(data) != 10:
        print("inválido. Digite novamente o que foi fornecido")
    elif conta_barra != 2:
        print("Inválido. Informe novamente o que foi fornecido")
    else:
        data_original = data.split("/")
        try:
          if len(data_original[0])  == 2 and len(data_original[1])  == 2 and len(data_original[2]) == 4:
              valido = valida_data(data_original)
              if valido:
                  print("DATA VALIDA")
                  continua = False
              else:
                  print("DATA INVÁLIDA")
          else:
              print("Data inválida. Informe novamente o que le foi informado!")
        except:
            print("error")
