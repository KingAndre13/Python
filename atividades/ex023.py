import random
al1 = input('*** Sorteio de alunos ***\nQual o nome do primeiro aluno?\n')
al2 = input('Qual o nome do segundo aluno?\n')
al3 = input('Qual o nome do terceiro aluno?\n')
al4 = input('Qual o nome do quarto aluno?\n')
alunos = [al1, al2, al3, al4]
numSort = random.randint(0, 3)
print('O aluno(a) sorteado(a) foi {}'.format(alunos[numSort]))