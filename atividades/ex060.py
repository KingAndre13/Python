option = 1
somaMedia = 0
didMedia = 0
numMedia = []

while option != 0:
    num = int(input('Digite um número: '))
    numMedia.append(num)
    somaMedia += numMedia[didMedia]
    didMedia += 1
    numMedia.sort()
    option = int(input('Você quer continuar?\n[0] Não\n[1] Sim\nEscolha: '))
print('A média de todos os números que você digitou foi {:.2f}'.format(somaMedia / didMedia))
print('O maior número foi {} e o menor número {}'.format(numMedia[didMedia-1], numMedia[0]))
