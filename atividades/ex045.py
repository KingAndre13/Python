from time import sleep
input('\033[1;34mÉ QUASE ANO NOVO\nAPERTE QUALQUER TECLA PARA COMEÇAR A CONTAGEM!!!\033[m')
for c in range(10, -1, -1):
    print('\033[1;33m{}\033[m'.format(c))
    sleep(1)
print('\033[1;31mFELIZ ANO NOVO!!!\033[m')
print('\033[1;35m{}\033[m'.format('BOom '*20))