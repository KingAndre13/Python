n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
cores = {'fecha':'\033[m', 'amarelo': '\033[33m', 'verde': '\033[32m' }
s = n1 + n2
print('A soma entre {}{} e {}{} vale {}{}{}'.format(cores['amarelo'], n1, n2, cores['fecha'], cores['verde'], s, cores['fecha']))