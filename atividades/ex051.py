frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
contrario = ''
contrario = junto[::-1]
'''for letra in range(len(junto) -1, -1, -1):
    contrario += junto[letra]'''
print('Sua frase: {}\nSua frase invertida: {}'.format(junto, contrario))
if junto == contrario:
    print('Essa frase é um palíndromo')
else:
    print('Essa frase não é um palíndromo')