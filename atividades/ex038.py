n1 = int(input('Digite 1° número: '))
n2 = int(input('Digite 2° número: '))

if n1 > n2 :
    print('1° valor: {} é maior'.format(n1))
elif n2 > n1 :
    print('2° valor: {} é maior'.format(n2))
else:
    print('Tanto o 1° valor quanto o 2° valor são iguais ({})'.format(n1))
