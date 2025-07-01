n1 = 0
n2 = 1
c = 0
numElem = int(input('Quantos elementos você quer ver da Sequência de Fibonacci: '))
while c < numElem:
    print('{}'.format(n1), end=' > ' )
    c+=1
    if c < numElem:
        print('{}'.format(n2), end=' > ')
        c+=1
    n1 = n1 + n2
    n2 = n1 + n2
   
print('Fim!')
        