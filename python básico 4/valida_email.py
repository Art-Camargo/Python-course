RED   = "\033[1;31m"  #código ANSI para cor vermelha
RESET = "\033[0;0m"   #código ANSI para resetar a saída com cor vermelha no terminal
#varáveis em maiúscula, representando a "imutabilidade" da var, pra não ser mudada
import os
def valida_email(email):
    if email.count("@") != 1 or email.rfind("@") == 0 \
    or email.rfind("@") == len(email) - 1:
        return False
    dominio_padrao = '.com'
    parte_dominio = email[email.rfind("@")::]
    if dominio_padrao not in parte_dominio:
        return False
    return True

valido = False
while not valido:
    email = input('Informe o seu email: ')
    os.system("cls")
    if valida_email(email):
        print(f'O email {email} é válido!!!!')
        valido = True
    else:
        print(f'O email {email} não é válido')
      
