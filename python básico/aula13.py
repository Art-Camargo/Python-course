#formats em strings 2
# orientado a objetos, função format
#formata pelo índice, tipo um array, da função
a = 'A'
b = 'B'
c = 1.1
string = 'a = {nome1}, b = {nome2}, c = {nome3:.2f}, {nome4}'
format = string.format(nome1 = a, nome2 = b, nome3 = c, nome4 = 'Amo a minha vida')

print(format, sep=" ", end="\n\n\n\n\n")