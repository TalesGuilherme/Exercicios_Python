n = int(input('Digite o primeiro termo da progressão: '))
r = int(input('Digite a razão(De quanto em quanto vai pular cada número): '))
decimo = n + (10 - 1) * r
for c in range(n, decimo + r, r):
    print(n, end=' ')
    n = n + r
print('\033[31mFIM', end='')
