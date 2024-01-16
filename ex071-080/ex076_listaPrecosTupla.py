listagem = ('Caneta', 1.50,
            'Lápis', 2.00,
            'Caderno pequeno', 12.00,
            'Caderno grande', 18.00,
            'Corretivo líquido', 8.00,
            'Apontador', 3.00,
            'Borracha', 4.50,
            'Estojo Ben 10', 7.50)

print('='*40)
print(f'{"LISTAGEM DE PREÇOS":^35}')
print('='*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:5.2f}')

print('='*40)
