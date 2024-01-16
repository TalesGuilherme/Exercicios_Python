from time import sleep

valor = int(input('Qual valor você deseja sacar? R$'))
ced50 = 0
ced20 = 0
ced10 = 0
ced1 = 0

while True:
    if valor - 50 >= 0:
        valor -= 50
        ced50 += 1
    else:
        if valor - 20 >= 0:
            valor -= 20
            ced20 += 1
        else:
            if valor - 10 >= 0:
                valor -= 10
                ced10 += 1
            else:
                if valor - 1 >= 0:
                    valor -= 1
                    ced1 += 1
                else:
                    break

for c in range(1, 30):
    print('-', end='')
    sleep(0.1)

if ced50 > 0:
    print(f'\n\033[32mTotal de cédulas de R$50 -> {ced50}\033[m')
if ced20 > 0:
    print(f'\n\033[33mTotal de cédulas de R$20 -> {ced20}\033[m')
if ced10 > 0:
    print(f'\n\033[34mTotal de cédulas de R$10 -> {ced10}\033[m')
if ced1 > 0:
    print(f'\n\033[35mTotal de cédulas de R$1 -> {ced1}\033[m')
