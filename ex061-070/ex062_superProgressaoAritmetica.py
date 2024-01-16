n = int(input('Digite o primeiro termo da progressão: '))
r = int(input('Digite a razão: '))
q = int(input('Digite a quantidade de termos: '))
acumuladorTermos = q
limite = 0
while not q == 0:
    print(n, end=' ')
    n = n + r
    q -= 1
    if q + 1 == 1:
        q = int(input('\nDeseja ver quantos termos a mais? '))
        acumuladorTermos += q

print('\n\033[31mFIM')
print('A quantidade de termos mostrados foi {}'.format(acumuladorTermos))
