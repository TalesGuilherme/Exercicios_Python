matriz = [[], [], []]
soma = 0
somaTerceiraCol = 0
maiorValorSeg = 0

while True:
    # Adicionando valores à matriz
    if len(matriz[0]) == 0:
        while len(matriz[0]) < 3:
            n = int(input(f'Digite um valor para [0, {len(matriz[0])}]: '))
            matriz[0].append(n)
            # Verificando se o número é par
            if n % 2 == 0:
                soma += n
    if len(matriz[1]) == 0:
        while len(matriz[1]) < 3:
            n = int(input(f'Digite um valor para [1, {len(matriz[1])}]: '))
            matriz[1].append(n)
            # Verificando se o número é par
            if n % 2 == 0:
                soma += n
    if len(matriz[2]) == 0:
        while len(matriz[2]) < 3:
            n = int(input(f'Digite um valor para [2, {len(matriz[2])}]: '))
            matriz[2].append(n)
            # Verificando se o número é par
            if n % 2 == 0:
                soma += n

    if len(matriz[2]) == 3:
        break

# Mostrando a matriz na tela:
print('-'*30)
for n in matriz[0]:
    print(f'[{n:^3}]', end='')
print('')
for n in matriz[1]:
    print(f'[{n:^3}]', end='')
print('')
for n in matriz[2]:
    print(f'[{n:^3}]', end='')
print('\n'+'-'*30)

# Mostrando a soma dos números pares:
print(f'A soma dos números pares é {soma}')
# Mostrando a soma dos valores da terceira coluna
somaTerceiraCol = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos elementos da terceira coluna é {somaTerceiraCol}')
# Mostrando o maior valor da segunda linha
maiorValorSeg = matriz[1][0]
if matriz[1][1] > maiorValorSeg:
    maiorValorSeg = matriz[1][1]
if matriz[1][2] > maiorValorSeg:
    maiorValorSeg = matriz[1][2]

print(f'O maior valor da segunda linha é {maiorValorSeg}')
