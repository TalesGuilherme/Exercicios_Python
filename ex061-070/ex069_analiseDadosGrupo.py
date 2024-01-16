from time import sleep

sexo = ''
continuar = ''
idade = 0
p = 1
maioresIdade = 0
homens = 0
mulheresMenores = 0

while True:
    idade = int(input(f'\nDigite a idade da {p}ª pessoa: '))
    sexo = str(input(f'Digite o sexo da {p}ª pessoa: [M/F]')).strip().upper()

    # Verificando se a entrada para "sexo" é válida
    if sexo != 'M' and sexo != 'F':
        while sexo != 'M' and sexo != 'F':
            print('\033[31mEntrada inválida!\033[m')
            sexo = str(input(f'Digite o sexo da {p}ª pessoa: [M/F]')).strip().upper()

    # Verificando se a pessoa é maior de idade
    if idade > 18:
        maioresIdade += 1

    # Verificando se é homem
    if sexo == 'M':
        homens += 1

    # Verificando mulheres com menos de 20 anos
    if sexo == 'F' and idade < 20:
        mulheresMenores += 1

    continuar = str(input('Você deseja continuar? [S/N]')).strip().upper()

    # Verificando se a entrada para "continuar é válida"
    if continuar != 'S' and continuar != 'N':
        while continuar != 'S' and continuar != 'N':
            print('\033[31mEntrada inválida!\033[m')
            continuar = str(input('Você deseja continuar? [S/N]')).strip().upper()

    # Encerramento do programa
    if continuar == 'N':
        break

    # Acumulador de quantas pessoas estão sendo registradas
    p += 1

for c in range(1, 30):
    print('-', end='')
    sleep(0.1)

print('\n\033[35mPROGRAMA ENCERRADO\033[m')
print(f'{maioresIdade} pessoas são maiores de idade.')
print(f'Foram cadastrados {homens} homens.')
print(f'Foram cadastradas {mulheresMenores} mulheres com menos de 20 anos.')
