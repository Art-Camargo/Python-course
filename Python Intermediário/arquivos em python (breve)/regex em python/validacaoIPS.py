#0.0.0.0 -> 255.255.255.255
import re

ip_reg = re.compile(r'''
    
''')

continua = True
while continua:
    ip_busca = input('Informe um Ip: ')
    if ip_reg.search(ip_busca):
        print(f'Ip {ip_busca} é válido')
        continua = False
    else:
        print(f'O Ip {ip_busca} é inválido')
        continua = True
