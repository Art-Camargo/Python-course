bruto = float(input('Informe o seu salário Bruto: '))
inss = bruto * 0.08
sindicato = bruto * 0.05
imposto = bruto * 0.11
descontos = bruto * 0.24
liquido = bruto - descontos
print(f'Salário bruto: {bruto:.2f}', end="\n\n")
print(f'Porcentagem do INSS: {inss:.2f}', end="\n\n")
print(f'Porcentagem do sindicato: {sindicato:.2f}', end="\n\n")
print(f'Porcentagem do imposto de renda fixa: {imposto:.2f}', end="\n\n")
print(f'total de descontos do salário: {descontos:.2f}', end="\n\n")
print(f'Valor líquido recebido: {liquido:.2f}')