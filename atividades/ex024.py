from random import shuffle
al1 = input('*** Ordem de apresentação ***\nQual o primeiro aluno?\n')
al2 = input('Qual o segundo aluno?\n')
al3 = input('Qual o terceiro aluno?\n')
al4 = input('Qual o quarto aluno?\n')
alunos = [al1, al2, al3, al4]
shuffle(alunos)
print('Ordem de apresentação: 1°{}, 2°{}, 3°{}, 4°{}'.format(alunos[0], alunos[1], alunos[2], alunos[3]))