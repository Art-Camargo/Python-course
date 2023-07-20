import re #regex (expressões regulares pro python)
#findall, search, sub, compile
string = 'Teste de expressões regulares, Teste'
print(re.search(r'Teste', string)) #retorna None caso não haja, Caso haja, retorna a posição de início e fim de onde está (index)

print(re.findall(r'Teste', string)) #retorna uma lista com todas as ocorreências, ou lista vazia
print(re.sub(r'Teste', 'TESTE', string)) #sub de substituição

regex = re.compile(r'TESTE')
 #recompila um regex
print(regex.search(string)) #busca o regex 'TESTE' na string
