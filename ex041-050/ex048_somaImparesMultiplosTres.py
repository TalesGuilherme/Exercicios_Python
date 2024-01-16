s = 0
cont = 0
for c in range(1, 501):
    if c % 2 != 0:
        if c % 3 == 0:
            print(c, end=' ')
            s += c
            cont += 1
print('\nA soma dos múltiplos de 3 (1 a 500) é: {}'.format(s))
print('São ao todo {} elementos.'.format(cont))
