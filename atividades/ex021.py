'''from math import pow, sqrt
cA = float(input('Digite o Cateto adjacente: '))
cO = float(input('Digite o Cateto oposto: '))
hipo = sqrt(pow(cA, 2) + pow(cO, 2))
print('O triângulo Retângulo com catetos {} e {} vai ter uma hipotenusa de {:.2f}'.format(cA, cO, hipo))'''
from math import hypot
cO = float(input('Digite o Cateto oposto: '))
cA = float(input('Digite o Cateto Adjacente: '))
hi = hypot(cO, cA)
print('A hipotenusa vai medir {:.2f}'.format(hi))