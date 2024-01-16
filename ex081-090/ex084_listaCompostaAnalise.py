dado = list()
pessoas = list()
maisPesados = list()
maisLeves = list()

cadastradas = 0
pesoAtual = 0
maiorPeso = 0
menorPeso = 0

while True:
    dado.append(str(input('Digite o nome: ')))
    dado.append(float(input('Digite o peso: ')))
    pesoAtual = dado[1]

    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()

    if continuar != 'S' and continuar != 'N':
        while True:
            print('\033[31mEntrada inválida!\033[m')
            continuar = str(input('Deseja continuar? [S/N]')).strip().upper()
            if continuar == 'S' or continuar == 'N':
                break

    pessoas.append(dado[:])

    if len(pessoas) == 2:
        maiorPeso = pesoAtual
        menorPeso = pesoAtual
    else:
        if pesoAtual > maiorPeso:
            maiorPeso = pesoAtual
        if pesoAtual < menorPeso:
            menorPeso = pesoAtual

    dado.clear()
    cadastradas += 1

    if continuar == 'N':
        break

print('-'*30)
# Mostrar quantas pessoas foram cadastradas
print(f'Foram cadastradas {cadastradas} pessoas.')

# Para mostrar as pessoas mais pesadas
for dado in pessoas:
    if dado[1] == maiorPeso:
        maisPesados.append(dado[0])
    if dado[1] == menorPeso:
        maisLeves.append(dado[0])

print(f'O maior peso é {maiorPeso}Kg. As pessoas que tem esse peso são: ', end='')
for p in maisPesados:
    print(f'{p}...', end=' ')
print(f'\nO menor peso é {menorPeso}Kg. As pessoas que tem esse peso são: ', end='')
for p in maisLeves:
    print(f'{p}...', end=' ')
