#flags e shorthands em python [À-ú] pega todos os acentos
#[a-zA-Z0-9À-ú] == \w
#[^a-zA-Z0-9À-ú] == \W
#[0-9] == \d
#[ \r\n\f\t] = tab, quebra linha, espaço
#lembrando, ao usar \letra, com a letra maiúsucla = negação
#\b = borsda (espaço em branco entre palavras)
#re.multiline -> ^ $
#re.dotall
import re
var_text = """
    João acordou de manhã com uma vontade irresistível de tomar café. 
    O aroma do café fresco invadia a cozinha e despertava seus sentidos. 
    Ele se dirigiu à cafeteira, 
    ansioso para saborear uma xícara da bebida que tanto apreciava. 
    Com cuidado, João escolheu seu copo favorito e, pacientemente, aguardou o café ser preparado. 
    Enquanto isso, ele imaginava o sabor rico e reconfortante que iria inundar seu paladar. 
    Finalmente, a cafeteira completou o ciclo e a xícara de café fumegante estava pronta para ser saboreada. 
    João pegou a xícara com as duas mãos e sentiu o calor reconfortante em seus dedos. 
    Ele deu um gole, apreciando cada gota e sentindo a cafeína lentamente despertar sua mente.
    Naquele momento, João percebeu que o café era o ritual matinal que impulsionava seu dia e trazia um sentimento de conforto e energia. 
    Com sua xícara em mãos, João estava pronto para enfrentar o que quer que o dia trouxesse.
"""
print(re.findall(r'\be\w+', var_text, flags=re.IGNORECASE))
print(re.findall(r'\b\w{3}e', var_text, flags=re.IGNORECASE)) #começa com espaço, tem 3 letras aleatórias no meio, ultima é E
