def soma(x, y):
    return x + y

def executa(funcao, *args):
    return funcao(*args)

def cria_multiplicador(numero):
    def multiplica(multiplicador):
        return multiplicador * numero
    return multiplica



soma_total = executa(lambda x, y: x + y, 2, 3) #lambda = def, parametros: o retorno e, talvez, o que vale cada parâmetro)
print(soma_total)
#refazer a função soma com lambda


duplica = executa(lambda n: lambda m: n * m, 3) #não usar lambda para coisas complexas, apenas para coisas simples
print(duplica(2))
