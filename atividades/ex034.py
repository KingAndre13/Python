r1 = float(input('Digite a 1° medida: '))
r2 = float(input('Digite a 2° medida: '))
r3 = float(input('Digite a 3° medida: '))
if(r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2):
    print('\033[1mCom essas medidas pode-se formar um triângulo!\033[m')
    if (r1 == r2 and r2 == r3) :
        print('\033[1;34mTipo do triângulo: \033[m\033[1;32mEquilátero\033[m')
    elif ( (r1 == r2 and r2 != r3) or (r2 == r3 and r3 != r1) or (r1 == r3 and r3 != r2) ) :
        print('\033[1;34mTipo do triângulo: \033[m\033[1;33mIsósceles\033[m')
    else :
        print('\033[1;34mTipo do triângulo: \033[m\033[1;31mEscaleno\033[m')
else:
    print('Com essas medidas não dá para formar um triângulo!')
