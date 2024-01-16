n = int(input('Digite um número inteiro: '))
resto = n % 2

if resto == 0 or n == 0:
    print('O número {} é PAR!'.format(n))
else:
    print('O número {} é IMPAR'.format(n))
