kmViagem = int(input('Qual vai ser a distância da sua viagem?\nKm:'))
if(kmViagem <= 200):
    print('A sua passagem vai custar R${:.2f}'.format(kmViagem * 0.50))
else:
    print('A sua passagem vai custar R${:.2f}'.format(kmViagem * 0.45))
'''
preco = kmViagem * 0.50 if kmViagem <= 200 else kmViagem * 0.45 
'''