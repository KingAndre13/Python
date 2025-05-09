import math
ang = int(input('Digite um ângulo: '))
rad = math.radians(ang)
print('O ângulo {}° tem um seno de {:.4f}, um coseno de {:.4f} e uma tangente de {:.4f}'.format(ang, math.sin(rad), math.cos(rad), math.tan(rad)))
