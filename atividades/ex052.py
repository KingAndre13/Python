from datetime import date
idades = []
for c in range(0, 7):
    anoNasc = int(input('Digite o ano de nascimento: '))
    idades.append(date.today().year - anoNasc)
cMaior = 0
cMenor = 0
for c in range(0, 7):
    if idades[c] >= 21:
        print('{}A {}° pessoa que tem a idade de {} anos é maior de idade.{}'.format('\033[1;32m', c+1, idades[c], '\033[m'))
        cMaior += 1
    else:
        print('{}A {}° pessoa que tem a idade de {} anos é menor de idade.{}'.format('\033[1;34m', c+1, idades[c], '\033[m'))
        cMenor += 1
print('Quantidades de Maiores de idade: {}'.format(cMaior))
print('Quantidades de Menores de idade: {}'.format(cMenor))
