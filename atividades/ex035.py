nome = 'Guanabara'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'petroebranco':'\033[7;37m'}
print('Olá! Muito prazer em te conhecer, {}{}{}'.format(cores['petroebranco'], nome, cores['limpa']))