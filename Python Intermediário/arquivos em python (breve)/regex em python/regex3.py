#teste de quantificadores no cpf
import re
conjunto_cpfs = '''
    055.165.260-86
    531.909.630-53
    111.111.111-11
    22222222222
    abcdefghijk
    222.313.222-85
'''
cpfs_validos = re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}', conjunto_cpfs) 
print(cpfs_validos)