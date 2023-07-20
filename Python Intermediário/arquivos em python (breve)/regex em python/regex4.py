#greedy e non-greedy
# * é qualquer coisa, tudo ou nada
# + é alguma coisa, tem que ter algo
import re
texto =  '''
<p>Frase 1</p> 
<p>Frase 2</p>
<div>Frase 3</div>
<div></div>
'''
print(re.findall(r'<[divp]{1,3}>.*<\/[divp]{1,3}>', texto)) #greedy, check todas as vezes essas ocasiões
print(re.findall(r'<[divp]{1,3}>.*?<\/[divp]{1,3}>', texto)) #greedy, check todas as vezes essas ocasiões
print(re.findall(r'<[divp]{1,3}>.+<\/[divp]{1,3}>', texto)) #greedy, check todas as vezes essas ocasiões
