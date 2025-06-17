n = int(input('Digite um número: '))
s = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[1;34m', end='')
        s += 1
    else:
        print('\033[1;31m', end='')
    print('{} '.format(c), end='')     
if s == 2 :
    print('\n{}O número {} é um número primo!!!{}'.format('\033[1;32m', n, '\033[m'))
else:
    print('\n{}O número {} NÃo é um número primo!!!{}'.format('\033[1;31m', n, '\033[m'))
    