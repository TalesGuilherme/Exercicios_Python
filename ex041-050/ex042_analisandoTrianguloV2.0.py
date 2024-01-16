print('Digite o valor de três retas, para verificar se há a possibilidade de se formar um triângulo')
n1 = float(input('Digite o valor da primeira reta: '))
n2 = float(input('Digite o valor da segunda reta: '))
n3 = float(input('Digite o valor da terceira reta: '))

if n1+n2 > n3 and n1+n3 > n2 and n2+n3 > n1:
    print('É possível formar um triângulo', end=' ')
    if n1 == n2 == n3:
        print('EQUILÁTERO(todos os lados iguais)')
    elif n1 != n2 != n3 != n1:
        print('ESCALENO(nenhum lado é igual)')
    else:
        print('ISÓSCELES(dois lados iguais)')
else:
    print('Não é possível formar um triângulo')

