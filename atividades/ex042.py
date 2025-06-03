alt = float(input('\033[1mBem-vindo ao Sistema de IMC\nDigite a sua Altura: \033[m'))
pes = float(input('\033[1mDigite o seu peso: \033[m'))

imc = pes / (pow(alt, 2))

print('\033[1;36mSeu IMC é de \033[1;35m{:.1f}kg/m²\033[m\n\033[1;36mE você de acordo com a tabela do IMC você está:\033[m'.format(imc))

if imc < 18.5 :
    print('\033[1;34mAbaxio do Peso.\033[m')
elif imc <= 25 :
    print('\033[1;32mNo Peso Ideal.\033[m')
elif imc <= 30 :
    print('\033[1;33mNo Sobrepeso\033[m')
elif imc <= 40 :
    print('\033[1;31mEm Obesidade\033[m')
else : 
    print('\033[1;41mEm Obesidade Mórbida\033[m')