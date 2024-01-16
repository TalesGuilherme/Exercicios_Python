numeros = list()
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

print('-'*30)
# Mostrar quantos números foram digitados na lista
print(f'Foram digitados {len(numeros)} números')

# Mostrar os números em ordem decrescente
numeros.sort(reverse=True)
print(f'A lista de valores em ordem decrescente: ', end='')
for n in numeros:
    print(f'{n}...', end='')

# Verificar se o número 5 foi escrito
if 5 in numeros:
    print('\nO número 5 foi digitado.')
else:
    print('\nO número 5 NÃO foi digitado')



