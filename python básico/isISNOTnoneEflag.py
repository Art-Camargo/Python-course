condicao = False
passou_if = None
if condicao:
    print(f'Esse é o if, pois a condição está do tipo {type(condicao)} no resultado {condicao}')
    passou_if = True
else:
    print(passou_if, passou_if is None, condicao is not None)
