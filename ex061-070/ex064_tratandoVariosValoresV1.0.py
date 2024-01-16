n = 0
q = 0
acumulador = 0

print('\nOBS: Para finalizar o programa digite o número 999\n')
while not n == 999:
    n = int(input('Digite um número inteiro: '))
    if n != 999:
        acumulador += n
        q += 1

print('\nForam digitados {} números.'.format(q))
print('A soma de todos os números digitados é igual a {}'.format(acumulador))
