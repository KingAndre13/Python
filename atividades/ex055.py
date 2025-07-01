sexoChosen = ''
while sexoChosen not in ('M', 'F') :
    sexoChosen = str(input('Digite o seu sexo:\n[M] - Masculino\n[F] - Feminino\nEscolha: ')).strip().upper()[0]
    if sexoChosen not in  ('M', 'F'):
        print('Digita Corretamente AÍ IRMÃO, NA MORAL!\nOU M PARA MASCULINO OU F PARA FEMININO')
        print('Digite novamente Caro Usuário\n |\n\_/\n')

if (sexoChosen == 'M'):
    print('Você escolheu o sexo Masculino!')
else:
    print('Você escolheu sexo Feminino!')
    