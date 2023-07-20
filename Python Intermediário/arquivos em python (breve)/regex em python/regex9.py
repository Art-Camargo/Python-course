import re
from pprint import pprint
# '.+' pega tudo, menos \n
# + é mais do que uma
ips = '''
  ONLINE 192.168.0.1 GHIJK active
  OFFLINE 192.168.0.2 GHIJK inactive
  OFFLINE 192.168.0.3 GHIJK active
  ONLINE 192.168.0.4 GHIJK active
  ONLINE 192.168.0.5 GHIJK inactive
  OFFLINE 192.168.0.6 GHIJK active
'''
print('Abaixo, todos os IPS ativos')
#positive lookahead (buscar se existe algo ?= )
pprint(re.findall(r'((?:\d{3}\.){2}\d.\d)(?:\s+\w+\s+)(?=active)', ips, flags=re.IGNORECASE)) #pega os ips linha a linha
# ?= só printa ou retorna se for igual (if ternário mais ou menos)
#retornou todos os actives
pprint(re.findall(r'(?=.*[^in]active).+', ips)) #outra maneira de achar os ativos


#negative lookahead
print('Abaixo, todos os IPS inativos')
pprint(re.findall(r'((?:\d{3}\.){2}\d.\d)(?:\s+\w+\s+)(?!active)', ips, flags=re.IGNORECASE)) #pega os ips linha a linha

#positive lookbehind nenhuma retorna a palavra, apenas verifica
pprint('Abaixo, todos os ips online')
pprint(re.findall(r'(?<= ONLINE)\s+((?:\d{3}\.){2}\d.\d)', ips))

#negative lookbehind
pprint(re.findall(r'(?<! ONLINE)\s+((?:\d{3}\.){2}\d.\d)', ips))
