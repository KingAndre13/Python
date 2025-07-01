n = int(input('Digite um número para ver o seu fatorial: '))
fat = n-1
soma = n
while fat > 1:
    soma = soma * fat
    fat-=1
print('{}!(fatorial) vai ser igual à {}'.format(n, soma))
