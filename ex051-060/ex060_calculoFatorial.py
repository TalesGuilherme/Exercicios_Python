n = int(input('Digite um número inteiro: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')

while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1

print('{}'.format(f))

# MÉTODO ALTERNATIVO PARA CALCULAR FATORIAL

# n = int(input('Digite um número inteiro: '))
# multiplicador = -1
# multi = 1

# while not multiplicador == 1:
# if multiplicador == -1:
# multiplicador = n
# multiplicador -= 1
# multi = n * multiplicador
# else:
# multiplicador -= 1
# multi *= multiplicador

# print('O resultado de {}! é igual a {}'.format(n, multi))
