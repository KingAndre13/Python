nome = input('Digite seu nome completo: ')
i = nome.split().count(nome)
print('Seu nome completo: {}\nPrimeiro nome: {}\nÚltimo nome: {}'.format(nome, nome.split()[0], nome.split()[i-1]))