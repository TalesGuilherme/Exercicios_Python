n = int(input('Digite um número inteiro: '))
print('Estes são os números pares entre 1 e {}:'.format(n))
for c in range(0, n+1, 2):
    print(c, end=' ')
print('FIM')
