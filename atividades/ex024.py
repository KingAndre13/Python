import random
input('*** Ordem de apresentação ***\nAperte qualquer tecla para executar!')
alunos = ['André', 'Eduarda', 'Sabrina', 'Juan']
random.shuffle(alunos)
print('Ordem de apresentação: 1°{}, 2°{}, 3°{}, 4°{}'.format(alunos[0], alunos[1], alunos[2], alunos[3]))