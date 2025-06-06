print('{:=^40}'.format('\033[1;34mLojas Guanabara\033[m'))
valorProduto = float(input('\033[1;35mDigite o preço das compras R$: '))
opcaoPagamento = int(input('''Como você gostaria de pagar:
1. À vista no Dinheiro/Cheque
2. À vista no Cartão
3. 2 vezes no Cartão
4. 3 vezes ou mais no cartão
Escolha à opção: \033[m'''))
vistaDinheirocheque = valorProduto - (valorProduto / 100 * 10)
vistaCartao = valorProduto - (valorProduto / 100 * 5)
duasParcelas = valorProduto / 2
if opcaoPagamento == 1 :
    print('\033[1mÀ vista no Dinheiro/Cheque o produto vai passar de \033[m\033[1;31mR${:.2f}\033[m\033[1m para \033[m\033[1;32mR${:.2f}\033[m'.format(valorProduto, vistaDinheirocheque))
elif opcaoPagamento == 2 :
    print ('\033[1mÀ vista no Cartão o produto vai passar de \033[m\033[1;31mR${:.2f}\033[m\033[1m para \033[m\033[1;32mR${:.2f}\033[m'.format(valorProduto, vistaCartao))
elif opcaoPagamento == 3 :
    print('\033[1mEm duas vezes no Cartão o produto ficar o mesmo preço de \033[m\033[1;34mR${:.2f}\033[m\033[1m 2x de \033[m\033[1;33mR${:.2f}\033[m'.format(valorProduto, duasParcelas))
elif opcaoPagamento == 4 :
    numParc = int(input('Quantas parcelas? : '))
    maisdeTresParcelas = (valorProduto + (valorProduto / 100 * 20)) / numParc
    print('\033[1mEm {} parcelas no Cartão o produto vai ter acréscimo de 20%, o produto vai ficar no valor total de \033[m\033[1;31mR${:.2f}\033[m\033[1m {}x de \033[m\033[1;33m{:.2f}\033[m'.format(numParc, maisdeTresParcelas * numParc, numParc, maisdeTresParcelas))
else :
    print('\033[1;31mOpção Inválida\033[m')
