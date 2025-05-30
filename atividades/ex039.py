from datetime import date
anoNasc = int(input('Qual o seu ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNasc

if idade < 18 :
    print('Você ainda vai se alistar!\nFaltam {} ano(s) para isso acontecer!'.format(18 - idade))
elif idade == 18 :
    print('Já está na hora de se alistar em {}!'.format(anoAtual))
else :
    print('Você já passou da hora de se alistar!\nJá se passaram {} ano(s) após o prazo!'.format(idade - 18))
