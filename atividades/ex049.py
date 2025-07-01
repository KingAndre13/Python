print('\033[1;34mBem vindo ao Programa de progressão aritmética')
Pa = int(input('Qual vai ser o primeiro termo: '))
razao = int(input('Qual vai ser a razão? : '))
arg = 10
c = 0
a = 0

while arg != 0 :
    c += arg 
    while a < c:
        print(Pa)
        Pa += razao
        a+=1
    arg = int(input('Quantos termos mais você quer que eu mostre? '))
print('\033[1;31mPrograma Encerrado com {} termos mostrados!!!\033[m'.format(c))
