'''tempo = int(input('Quantos anos tem seu carro?\n'))
print('Carro novo'if tempo <=3 else'Carro velho')
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')
///////////////////////////////////////
nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
    print('Bom dia, {}!'.format(nome))
//////////////////////////////////////
'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
'''if m >= 6:
    print('Aprovado!')
else:
    print('Reprovado!')'''
print('Aprovado!' if m >=6 else 'Reprovado!')