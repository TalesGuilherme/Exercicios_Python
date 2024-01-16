soma = 0
contador = 0
continuar = ''
maior = 0
menor = 0

while not continuar == 'N':
    n = int(input('Digite um número inteiro: '))
    if contador == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    contador += 1
    soma += n
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()

    if continuar != 'S' and continuar != 'N':
        while continuar != 'S' and continuar != 'N':
            print('\033[31mEntrada inválida!\033[m')
            continuar = str(input('Deseja continuar? [S/N]')).strip().upper()


media = soma / contador
print('\nA media dos números digitados é igual a {:.1f}'.format(media))
print('O maior valor lido foi {}'.format(maior))
print('O menor valor lido foi {}'.format(menor))
