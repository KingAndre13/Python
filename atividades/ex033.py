salFun = float(input('Digite o salário do Funcionário(a)\nR$:'))
if(salFun >= 1250.00):
    SalAum = ((salFun / 100 * 10) + salFun)
    print('Com o aumento de 10% ' 'salário desse Funcionário(a) vai passar de R${:.2f} para R${:.2f}'.format(salFun, SalAum))
else:
    SalAum = ((salFun / 100 * 15) + salFun)
    print('Com o aumento de 15% ' 'salário desse Funcionário(a) vai passar de R${:.2f} para R${:.2f}'.format(salFun, SalAum))