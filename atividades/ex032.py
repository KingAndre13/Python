n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))
# Verificando quem é menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando quem é menor
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor: {}'.format(menor))
print('O maior valor: {}'.format(maior))
'''
if (n1 > n2 > n3):
    print('Maior: {}\nMenor: {}'.format(n1, n3))
elif(n3 > n2 > n1):
    print('Maior: {}\nMenor: {}'.format(n3, n1))
elif(n2 > n3 > n1):
    print('Maior: {}\nMenor: {}'.format(n2, n1))
elif(n1 > n3 > n2):
    print('Maior: {}\nMenor: {}'.format(n1, n2))
elif(n3 > n1 > n2):
    print('Maior: {}\nMenor: {}'.format(n3, n2))
elif(n2 > n1 > n3):
    print('Maior: {}\nMenor: {}'.format(n2, n3))
'''