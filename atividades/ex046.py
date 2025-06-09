input('Aperte qualquer tecla para começar a contagem')
for c in range(2, 51, 2):
    print('{}{}{}'.format('\033[1;34m', c,'\033[m'))