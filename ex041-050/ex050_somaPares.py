from time import sleep

sp = 0
si = 0

print('Digite ao todo 6 números inteiros')
print('='*30)
for c in range(0, 6):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        sp += n
    else:
        si += n

for d in range(0, 30):
    sleep(0.1)
    print('=', end='')

print('\nO resultado da soma dos números pares é {}'.format(sp))
print('O resultado da soma dos números ímpares é {}'.format(si))
