from datetime import date
anoBi = int(input('Digite um ano qualquer(digite 0 para mostrar o ano atual): '))
if(anoBi == 0):
    anoBi = date.today().year
if(anoBi%4 == 0 and anoBi%100 != 0 or anoBi%400 == 0):
    print('O ano {} é um ano Bissexto!'.format(anoBi))
else:
    print('O ano {} não é um ano Bissexto!'.format(anoBi))