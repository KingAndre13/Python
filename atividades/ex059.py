soma = n = c = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        soma += n
        c+=1
print('Foram digitados {} números é a soma total entre eles deu {}'.format(c, soma))
