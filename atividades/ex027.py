from random import randint
n = int(input('Digite um número de (0 à 5): '))
nAl = randint(0, 5)
print('Seu Número: {}\nNúmero do Computador: {}\nVocê venceu!'.format(n, nAl) if n == nAl else 'Seu Número: {}\nNúmero do Computador: {}\nVocê Perdeu!'.format(n, nAl))