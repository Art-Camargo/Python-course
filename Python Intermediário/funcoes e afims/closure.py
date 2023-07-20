def boas_vindas_e_nome(string):
    def saudacao(nome):
        return f'{nome}, {string}'
    return saudacao


bom_dia = boas_vindas_e_nome('Bom dia')
boa_noite = boas_vindas_e_nome('Boa noite')
for nomes in ['Artur de Camargo', 'José Camargo', 'Maria Júlia']:
    print(bom_dia(nomes))
    print(boa_noite(nomes))


#um pouco associado a ponteiros em C!