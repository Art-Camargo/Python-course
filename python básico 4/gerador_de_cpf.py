import random #randint pra inteiro (random int)
def obtem_digitos_finais(cpf):
    count = 0
    j = len(cpf) + 1
    for index_digito in cpf:
        count += int(index_digito) * j
        j -= 1
    if count % 11 < 2:
        return 0
    else:
        return 11 - (count % 11)
for k in range (10**2): #100 cpfs válidos
    cpf = ''
    for i in range(9):
        cpf += str(random.randint(0, 9))
    cpf += str(obtem_digitos_finais(cpf)) 
    cpf += str(obtem_digitos_finais(cpf)) 
    print(cpf)