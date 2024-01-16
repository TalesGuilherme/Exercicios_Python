matriz = [[], [], []]

while True:
    if len(matriz[0]) == 0:
        while len(matriz[0]) < 3:
            n = int(input(f'Digite um valor para [0, {len(matriz[0])}]: '))
            matriz[0].append(n)
    if len(matriz[1]) == 0:
        while len(matriz[1]) < 3:
            n = int(input(f'Digite um valor para [1, {len(matriz[1])}]: '))
            matriz[1].append(n)
    if len(matriz[2]) == 0:
        while len(matriz[2]) < 3:
            n = int(input(f'Digite um valor para [2, {len(matriz[2])}]: '))
            matriz[2].append(n)

    if len(matriz[2]) == 3:
        break

print('-'*30)

for n in matriz[0]:
    print(f'[{n:^3}]', end='')
print('')

for n in matriz[1]:
    print(f'[{n:^3}]', end='')
print('')

for n in matriz[2]:
    print(f'[{n:^3}]', end='')
