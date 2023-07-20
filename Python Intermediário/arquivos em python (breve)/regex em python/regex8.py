import re
todos_cpfs = '''
    017.605.765-06 
    769.457.868-89
    210.535.760-13
    827.864.438-14
    755.847.564-31
    403.516.211-64
    775.669.287-08
    899.998.754-08
'''
cpf_validos = re.sub(r'\.|-', '', todos_cpfs)
cpf_validos = re.findall(r'\d{11}', cpf_validos)
print(cpf_validos)