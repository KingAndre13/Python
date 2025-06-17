mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totMulher20 = 0
for p in range(1, 5):
    print('{} {}° PESSOA {}'.format('-'*5, p, '-'*5))
    nomes = str(input('Nome: ')).strip()
    idades = int(input('Idade: '))
    sexos = str(input('Sexo [M/F]: ').upper().strip())
    mediaIdade += idades
    if p == 1 and sexos == 'M':
        maiorIdadeHomem = idades
        nomeVelho = nomes
    if sexos == 'M' and idades > maiorIdadeHomem:
        maiorIdadeHomem = idades
        nomeVelho = nomes
    if sexos == 'F' and idades < 20:
        totMulher20 =+ 1
mediaIdade = mediaIdade/4
print('A média de idade do grupo é de {} anos'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maiorIdadeHomem, nomeVelho))
print('Temos {} Mulheres com menos de 20 anos'.format(totMulher20))