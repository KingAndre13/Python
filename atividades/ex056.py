from time import sleep
opcao = 1
n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
while opcao !=5:
    print('O que você quer fazer com esses dois número?')
    print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
    opcao = int(input('Escolha a opção: '))
    if opcao == 1:
        print('Você escolheu a opção de Somar')
        print('A Soma entre {} e {} é igual à {}'.format(n1, n2, n1+n2))
    elif opcao == 2:
        print('Você escolheu a opção de Multilicar')
        print('A Multiplicação entre {} e {} é igual à {}'.format(n1, n2, n1*n2))
    elif opcao == 3:
        print('Você escolheu a opção Maior')
        if n1 == n2:
            print('Ambos os números {} e {} são iguais!'.format(n1, n2))
        elif n1 > n2:
            print('O Maior número entre {} e {} é {}'.format(n1, n2, n1))
        else:
            print('O Maior número entre {} e {} é {}'.format(n1, n2, n2))
    elif opcao == 4:
        n1 = int(input('Digite o 1° número: '))
        n2 = int(input('Digite o 2° número: '))
    elif opcao > 5 or opcao < 1:
        print('Opção Inválida! Tente novamente!')
print('Fechando as janelas...')
sleep(2)
print('Interrompendo execuções...')
sleep(2)
print('Saindo em 3...')
sleep(1)
print('Saindo em 2...')
sleep(1)
print('Saindo em 1...')
    