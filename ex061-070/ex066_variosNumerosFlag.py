n = 0
cont = 0
soma = 0

while True:
    n = int(input('Digite um número inteiro (999 para encerrar): '))
    if n == 999:
        break
    cont += 1
    soma += n

print('='*30)
print(f'Foram digitados {cont} números.')
print(f'A soma entre eles é igual a {soma}')
