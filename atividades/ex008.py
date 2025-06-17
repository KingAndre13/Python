n = int(input('Digite um número: '))
print('A Tabuada de {} é essa:'.format(n))
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n*c))
