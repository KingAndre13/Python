resultado = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}° número: '.format(c)))
    if num % 2 == 0:
        resultado += num
        cont += 1
print('Você informou {} números pares e a soma foi {}'.format(cont, resultado))
    