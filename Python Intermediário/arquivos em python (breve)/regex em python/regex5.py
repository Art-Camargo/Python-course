
#[a-zA-Z]+
#(...) grupo
import re
from pprint import pprint
texto =  '''
<p>Frase 1</p> 
<p>Frase 2</p>
<div>Frase 3</div>
<div></div>
'''

tags = re.findall(r'<([divp]{1,3})>(.+?)<\/\1>', texto) 
#greedy, check todas as vezes essas ocasiões
pprint(tags)

#nova      forma pra cpf? 
cpf = '055.165.260-86'
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))
# ?: ignora e não salva