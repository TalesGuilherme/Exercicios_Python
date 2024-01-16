numeros = [[], []]

for c in range(0, 7):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        numeros[0].append(n)
    if n % 2 != 0:
        numeros[1].append(n)

numeros[0].sort()
numeros[1].sort()

print('-'*30)
print(f'Lista de números pares: {numeros[0]}')
print(f'Lista de números ímpares: {numeros[1]}')
