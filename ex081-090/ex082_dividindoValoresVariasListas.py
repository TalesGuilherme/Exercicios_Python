numeros = list()
pares = list()
impares = list()
continuar = ''

while True:
    numeros.append(int(input('Digite um número inteiro: ')))

    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()

    if continuar != 'S' and continuar != 'N':
        while True:
            print('\033[31mEntrada inválida!\033[m')
            continuar = str(input('Deseja continuar? [S/N]')).strip().upper()
            if continuar == 'S' or continuar == 'N':
                break

    if continuar == 'N':
        break

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print('-'*30)

# Lista digitada pelo usuário
print(f'A lista digitada: {numeros}')

# Lista contendo os números pares digitados
if len(pares) > 0:
    print(f'A lista de números pares: {pares}')
else:
    print('Não foram digitados números pares.')

# Lista contendo os números impares digitados
if len(impares) > 0:
    print(f'A lista de números impares: {impares}')
else:
    print('Não foram digitados números impares')
