from math import pow, sqrt
cA = int(input('Digite o Cateto adjacente: '))
cO = int(input('Digite o Cateto oposto: '))
hipo = sqrt(pow(cA, 2) + pow(cO, 2))
print('O triângulo Retângulo com catetos {} e {} vai ter uma hipotenusa de {}'.format(cA, cO, hipo))