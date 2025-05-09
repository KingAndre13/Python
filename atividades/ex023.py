import random
input('*** Sorteio de alunos ***\n1.Gabriel\n2.Juan\n3.Eduarda\n4.André\nO programa vai escolher o aluno sorteado\nAperte qualquer tecla para executar!')
alunos = ['André', 'Juan', 'Eduarda', 'Gabriel']
numSort = random.randint(0, 3)
print('O aluno(a) sorteado(a) foi {}'.format(alunos[numSort]))