valorImovel = float(input('\033[34mBem-Vindo ao Programa de Finaciamento Imobiliário do Banco GB\033[m\n\033[32mQual o valor do imovél que você quer comprar?\033[m\n'))
salarioCredor = float(input('\033[32mQual o valor da sua renda?\033[m\n'))
periodParcl = int(input('\033[32mE em quantos anos você deseja pagar o imovél?\033[m\n'))
parclEmprestimo = valorImovel / (periodParcl * 12)
porcenParcl = salarioCredor/100 * 30

if (parclEmprestimo > porcenParcl) :
    print('\033[32mInfelizmente seu finaciamento foi \033[31mNEGADO\033[m\033[32m em nossa análise!\033[m')
else:
    print('\033[33mParabéns, seu financiamento foi \033[32mAceito\033[m\033[33m após nossa análise\033[m')
    print('\033[33mVai ficar {} parcelas de R${:.2f}\033[m'.format(periodParcl * 12, parclEmprestimo))