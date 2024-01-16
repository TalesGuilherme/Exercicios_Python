from math import trunc

n = float(input('Digite um número decimal (utilizando "." no lugar da vírgula): '))
print('O número decimal digitado foi: {}'.format(n))
print('O número {} na porção inteira é {}'.format(n, trunc(n)))
