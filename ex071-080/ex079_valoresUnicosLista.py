numeros = list()
continuar = ''

while True:
    n = int(input('Digite um número inteiro: '))
    if n not in numeros:
        numeros.append(n)
    else:
        print('\033[31mNúmero repetido! Não será adicionado.\033[m')

    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()

    if continuar != 'S' and continuar != 'N':
        while True:
            print('\033[31mEntrada inválida!\033[m')
            continuar = str(input('Deseja continuar? [S/N]')).strip().upper()
            if continuar == 'S' or continuar == 'N':
                break

    if continuar == 'N':
        break

print('-'*30)

print('A lista em ordem crescente: ', end='')
for n in sorted(numeros):
    print(f'{n}', end=' ')

