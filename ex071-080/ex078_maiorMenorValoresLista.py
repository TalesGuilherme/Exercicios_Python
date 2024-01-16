numeros = [int(input('Digite um número inteiro: ')), int(input('Digite um número inteiro: ')),
           int(input('Digite um número inteiro: ')), int(input('Digite um número inteiro: ')),
           int(input('Digite um número inteiro: '))]

print('-'*30)
print(f'Sua lista é {numeros}')
# Mostra a posição na qual se encontram os números digitados
for pos, n in enumerate(numeros):
    print(f'O número \033[32m{n}\033[m está na posição {pos}')
print('-'*30)

# Mostra qual é o MAIOR valor digitado e suas posições na lista (Caso se repitam)
print(f'O maior valor é \033[33m{max(numeros)}\033[m nas posições ', end='')
for pos, num in enumerate(numeros):
    if num == max(numeros):
        print(f'{pos}...', end=' ')

# Mostra qual é o MENOR valor digitado e suas posições na lista (Caso se repitam)
print(f'\nO menor valor é \033[34m{min(numeros)}\033[m nas posições ', end='')
for pos, num in enumerate(numeros):
    if num == min(numeros):
        print(f'{pos}...', end=' ')
