n = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[34m{}'.format(c), end=' ')
        tot += 1
    else:
        print('\033[31m{}'.format(c), end=' ')
    # print('{}'.format(c), end=' ')
if tot == 2:
    print('\n\033[32mO número {} foi divisível 2 vezes'.format(n))
    print('\033[34mNÚMERO PRIMO!')
else:
    print('\n\033[32mO número {} foi divisível {} vezes'.format(n, tot))
    print('\033[31mESSE NÚMERO NÃO É PRIMO!')
