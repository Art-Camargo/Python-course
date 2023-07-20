s1 = set('Artur de Camargo')#não garante a ordem
print(s1, type(s1))
s2 = { 
    'Luiz', 'Artur'
}
print(s2) #não aceita lista ou dicionário dentro
s3 = (5,5,5,5,2,2,2,2,3,3,3,3,3)
print(s3) #eliminam, por padrão, valores duplicados
tup = sorted(set(s3)) #não tem indices
print(tup)
#aceita iterações (is, in, for)