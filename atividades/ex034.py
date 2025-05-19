r1 = float(input('Digite a 1° medida: '))
r2 = float(input('Digite a 2° medida: '))
r3 = float(input('Digite a 3° medida: '))
if(r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2):
    print('Com essas medidas pode-se formar um triângulo!')
else:
    print('Com essas medidas não dá para formar um triângulo!')
