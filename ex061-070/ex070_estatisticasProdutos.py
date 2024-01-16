from time import sleep

nome = ''
nomeMenor = ''
continuar = ''
valor = 0
totalGasto = 0
maisMil = 0
menor = maior = 0
contador = 0

while True:
    nome = str(input('\nDigite o nome do produto: ')).strip()
    valor = float(input('Digite o valor do produto: R$'))

    contador += 1

    totalGasto += valor

    if valor > 1000:
        maisMil += 1

    if contador == 1 or valor < menor:
        menor = valor
        nomeMenor = nome

    # Verificando se o usuário deseja continuar
    continuar = str(input('Você deseja continuar? [S/N]')).strip().upper()

    if continuar != 'S' and continuar != 'N':
        while continuar != 'S' and continuar != 'N':
            print('\033[31mEntrada inválida!\033[m')
            continuar = str(input('Você deseja continuar? [S/N]')).strip().upper()

    if continuar == 'N':
        break

print('-'*30)
print('\033[35mGERANDO RESULTADO\033[m')
for c in range(1, 30):
    print('-', end='')
    sleep(0.1)

print(f'\nO total gasto na compra foi R${totalGasto:.2f}')
print(f'{maisMil} produtos custam mais de R$1000,00')
print(f'O produto mais barato é {nomeMenor} e custa R${menor:.2f}')
