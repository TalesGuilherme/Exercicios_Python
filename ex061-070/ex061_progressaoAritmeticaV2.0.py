n = int(input('Digite o primeiro termo de uma progressão: '))
r = int(input('Digite a razão: '))
q = int(input('Digite a quantidade de termos: '))
limite = 0
while not limite == q:
    print(n, end=' ')
    n = n + r
    limite += 1
print('\033[31mFIM')














