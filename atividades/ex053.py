pesos = []
for c in range(1, 6):
    pesos.append(float(input('Digite o peso da {}° pessoa: '.format(c))))
    pesos.sort()
print('O maior peso foi {:.1f}Kg\nE o menor peso foi {:.1f}Kg'.format(pesos[4], pesos[0]))
