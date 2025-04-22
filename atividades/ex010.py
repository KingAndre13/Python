alturaParede = float(input('Qual é a altura da parede?\n'))
larguraParede = float(input('Qual é a largura da parede?\n'))
areaParede = alturaParede*larguraParede
print('A Àrea da parede é de {:.1f}m²\nPara pintar a sua parede você irá precisar de {:.1f} litros de tinta!'.format(areaParede, areaParede/2))