
def modifica_x():
    global x #sem usar global, má prática
    x = 15
def modifica_string(string):
    string = string.capitalize()
    return string

def modifica_vetor(vetor):
    j = 0
    for i in range(35, 40):
        vetor[j] = i
        j += 1
vetor = ['1', '2', '3', '4', '5']    
x = 10
print(f'{x=}')
modifica_x()
print(f'{x=}')
string = 'ARTUR DE CAMARGO'
string = modifica_string(string)
print(f'{string=}')
modifica_vetor(vetor)
print(vetor)

