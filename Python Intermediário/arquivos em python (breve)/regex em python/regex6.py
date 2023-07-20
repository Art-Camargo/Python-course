#meta chars ^ e $ começa com e termina com
# ^ -> começa com
# $ -> termina com
# [^a-z] -> nega, qualquer coisa que não seja entre a-z
# [0-9^] -> pega, quando achar algo diferenete, para e armazena em unma lista
import re
cpf = '055.165.260-86'
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
