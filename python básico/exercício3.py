name = 'Artur de Camargo'
#Exercício de formatação com função e parâmetros
idade = 20
uni = 'UERGS'
course = 'Universidade Estadual do Rio Grande do  Sul'
namorada = 'Eduarda'
mae = 'Jurema'

string = 'Nome: {name}; Idade: {id}; Universidade: {un}; Curso: {course}; Namorada: {namo}; Nome da mãe: {mae}'
formatar = string.format(name = name, id = idade, un = uni, course = course, namo = namorada, mae = mae)
print(formatar, end="\n\n")
print("Nome da minha namorada, com as duas primeiras letras = {}", namorada[0 : 2])