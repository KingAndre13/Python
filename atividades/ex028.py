velo = int(input('Qual foi a velocidade: '))
multa = None
if (velo > 80):
    multa = (velo - 80) * 7
    print('*** MULTADO ***\nVelocidade acima da estipulada:{}km/h\nValor da Multa:\nR$:{:.2f}'.format(velo, multa))
else:
    print('Velocidade dentro do estipulado!!!')