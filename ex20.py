from random import shuffle

a = str(input('Primeiro aluno? '))
b = str(input('Segundo aluno? '))
c = str(input('Terceiro aluno? '))
d = str(input('Quarto aluno? '))

alunos = [a,b,c,d]
shuffle(alunos)

print(f'A ordem de apresentação será: {alunos[0]}, {alunos[1]}, {alunos[2]} e {alunos[3]}')
# print(f'A ordem de apresentação será: ')
# print(alunos)