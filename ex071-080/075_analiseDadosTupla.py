n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
n4 = int(input('Digite o quarto valor: '))
numeros = n1, n2, n3, n4

print(f'\nO valor 9 apareceu {numeros.count(9)} vezes.')

if numeros.count(3) > 0:
    print(f'O primeiro valor 3 foi digitado na {numeros.index(3)+1}ª posição')
else:
    print('Não foi digitado nenhum valor 3')

print('Os números pares são: ', end='')
for numero in numeros:
    if numero % 2 == 0:
        print(numero, end=' ')
