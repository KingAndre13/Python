from random import randint
from time import sleep
n = int(input('Digite um número de (0 à 5): '))
nAl = randint(0, 5)
print('Processando...')
sleep(3)
print('-=-'*20)
print('Seu Número: {}\nNúmero do Computador: {}\nVocê venceu!'.format(n, nAl) if n == nAl else 'Seu Número: {}\nNúmero do Computador: {}\nVocê Perdeu!'.format(n, nAl))
print('-=-'*20)