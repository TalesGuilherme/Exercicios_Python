ext = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
continuar = ''

while True:
    n = int(input('Digite um número inteiro (0, 20): '))

    while not 20 >= n >= 0:
        print('\033[31mNúmero inválido!\033[m')
        n = int(input('Digite um número inteiro (0, 20): '))

    for pos, numero in enumerate(ext):
        if n == pos:
            print(f'\033[34mVocê digitou o número {numero}\033[m')

    continuar = str(input('Você deseja continuar? [S/N]')).strip().upper()

    if continuar != 'S' and continuar != 'N':
        while True:
            print('\033[31mEntrada inválida!\033[m')
            continuar = str(input('Você deseja continuar? [S/N]')).strip().upper()
            if continuar == 'S' or continuar == 'N':
                break

    if continuar == 'N':
        break

print('\n\033[34mPrograma encerrado')
