from random import randint
from time import sleep
numTen = 0
n = -1
nAl = randint(0, 10)
while n != nAl:
    n = int(input('Digite um número de (0 à 10): '))
    print('Processando...')
    sleep(1)
    if n!=  nAl:
        if n < nAl:
            print('-=-'*20)
            print('Mais... Tente Novamente!')
            print('-=-'*20)
        else:
            print('-=-'*20)
            print('Menos... Tente Novamente!')
            print('-=-'*20)
    numTen+=1
print('Seu Número: {}\nNúmero do Computador: {}\nVocê venceu!'.format(n, nAl))
print('Você precisou de {} tentativas para obter à vitória!'.format(numTen))
