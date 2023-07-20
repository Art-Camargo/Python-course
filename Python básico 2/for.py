phrase = 'Euamoaminhavida'
ast = ''
calc = len(phrase) - 1
for i in phrase:
    ast += f'*{i.upper()}'
print(ast, '*', sep="")