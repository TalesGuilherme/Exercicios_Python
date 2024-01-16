from random import randint
from time import sleep

jogador = ''
resultado = ''
logica = ''

n = 0
computador = 0
soma = 0
cont = 0


while True:
    n = int(input('Digite um valor: '))
    jogador = str(input('Par ou Ímpar? [P/I] ')).strip().upper()

    if jogador != 'P' and jogador != 'I':
        while jogador != 'P' and jogador != 'I':
            print('\033[31mEntrada inválida!\033[m')
            jogador = str(input('Par ou Ímpar? [P/I]')).strip().upper()

    computador = randint(0, 10)
    soma = n + computador
    for c in range(1, 30):
        print('-', end='')
        sleep(0.1)
    print(f'\nVocê jogou {n} e o computador {computador}')

    if soma % 2 == 0:
        resultado = 'P'
        logica = 'PAR'
    else:
        resultado = 'I'
        logica = 'ÍMPAR'

    print(f'A soma de ambos é igual a {soma}, portanto {logica}')

    if jogador == resultado:
        print('\033[33mVocê ganhou +1 ponto\033[m\n')
        cont += 1
    else:
        print('Não foi dessa vez...')
        break

if cont == 0:
    print('\n\033[31mVocê não venceu NENHUMA vez...\033[m')

else:
    print(f'\n\033[34mO número de vitórias foi {cont}\033[m')
