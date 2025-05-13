''' Resolução que eu fiz!
import math
ang = int(input('Digite um ângulo: '))
rad = math.radians(ang)
print('O ângulo {}° tem um seno de {:.2f}, um coseno de {:.2f} e uma tangente de {:.2f}'.format(ang, math.sin(rad), math.cos(rad), math.tan(rad)))'''

from math import radians, sin, cos, tan

an = float(input('Digite o ângulo que você deseja: '))

sen = sin(radians(an))
cose = cos(radians(an))
tang = tan(radians(an))

print('O ângulo {:.0f}° tem um seno de {:.2f}, um coseno de {:.2f} e uma tangente de {:.2f}'.format(an, sen, cose, tang))
