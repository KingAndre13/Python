numInt = int(input('Digite um número inteiro: '))
opcaoUsuario = int(input('Escolha uma das bases para conversão:\n[ 1 ] converter para Binário\n[ 2 ] converter para Octal\n[ 3 ] converter para Hexadecimal\nSua opção: '))

if opcaoUsuario == 1 :
    print('{} convertido para binário é igual a {}'.format(numInt, bin(numInt)[2:]))
elif opcaoUsuario == 2 :
    print('{} convertido para octal é igual a {}'.format(numInt, oct(numInt)[2:]))
elif opcaoUsuario == 3 :
    print('{} covertido para hexadecimal é igual a {}'.format(numInt, hex(numInt)[2:]))
else:
    print('Opção Inválida!')