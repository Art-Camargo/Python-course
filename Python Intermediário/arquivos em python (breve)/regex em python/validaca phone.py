import re
numeros = ['21 9 88525214', '54 9 81248316', '21 9 8852-5214'] 
numero_reg = re.compile(r'''
    (?:
       ^\d{2}\s+\d\s*\d{4}-\d{4}$ #+ precisa (1 ou mais), * nao precisa (0 ou mais)
                    |
       ^\d{2}\s+\d\s*\d{4}\d{4}$               
    )
''', flags=re.VERBOSE)
print('Telefones válidos abaixo')
for numero in numeros:
    if re.findall(numero_reg, numero):
        print(numero, end="  ")