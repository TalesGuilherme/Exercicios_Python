n = int(input('Digite um número inteiro: '))
print('Tabuada do 1 ao 10')
print('='*12)
for c in range(1, 11):
    tab = c
    res = n * tab
    print('{} x {} = {}'.format(n, tab, res))
print('='*12)
