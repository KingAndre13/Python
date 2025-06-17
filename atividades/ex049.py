print('\033[1;34mBem vindo ao Programa de progressão aritmética')
prinTermo = int(input('Qual vai ser o primeiro termo: '))
razao = int(input('Qual vai ser a razão? : '))
decimo = prinTermo + (10-1) * razao
for c in range(prinTermo, decimo + razao, razao):
    print(c)