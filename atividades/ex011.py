precoProduto = float(input('Qual é o preço do produto?\nR$:'))
print('Esse produto que está por R${:.2f} estar na promoção de 5% por R${:.2f}'.format(precoProduto, precoProduto - precoProduto/20))