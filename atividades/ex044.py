from random import randint

opcaoJogador = int(input('\033[1;33mBem-Vindo ao Jokenpô Game\nEscolha com o que você vai jogar contra o computador!\n1.Pedra\n2.Papel\n3.Tesoura\nEscolha: \033[m'))
opcaoComputador = randint(1, 3)
personagens = ['Pedra', 'Papel', 'Tesoura']

if (opcaoJogador < 1 or opcaoJogador > 4) :
    print('\033[1;31mOpcão Inválida!\033[m')
else:
    if (opcaoJogador == opcaoComputador) :
        print('\033[1;34mSua Escolha: {}\033[m'.format(personagens[opcaoJogador-1]))
        print('\033[1;34mEscolha do computador: {}\033[m'.format(personagens[opcaoComputador-1]))
        print('\033[1;33mNesta rodada, você empatou!\033[m')
    elif ( (opcaoJogador == 1 and opcaoComputador == 3) or (opcaoJogador == 2 and opcaoComputador == 1) or (opcaoJogador == 3 and opcaoComputador == 2)) :
        print('\033[1;34mSua Escolha: {}\033[m'.format(personagens[opcaoJogador-1]))
        print('\033[1;34mEscolha do computador: {}\033[m'.format(personagens[opcaoComputador-1]))
        print('\033[1;32mNesta rodada, você Venceu!!!\033[m')
    elif ( (opcaoJogador == 1 and opcaoComputador == 2) or (opcaoJogador == 2 and opcaoComputador == 3) or (opcaoJogador == 3 and opcaoComputador == 1)) :
        print('\033[1;34mSua Escolha: {}\033[m'.format(personagens[opcaoJogador-1]))
        print('\033[1;34mEscolha do computador: {}\033[m'.format(personagens[opcaoComputador-1]))
        print('\033[1;31mNesta rodada, você Perdeu!\033[m')
