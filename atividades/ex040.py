nota1 = float(input('Digite a sua 1° nota: '))
nota2 = float(input('Digite a sua 2° nota: '))
media = (nota1 + nota2) / 2

print('\033[1;35mMédia: {:.2f}\033[m'.format(media))

if media < 5.0:
    print('\033[1;31mReprovado!\033[m')
elif media <= 6.9:
    print('\033[1;33mRecuperação!\033[m')
else:
    print('\033[1;32mAprovado!\033[m')
