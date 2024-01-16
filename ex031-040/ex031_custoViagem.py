d = float(input('Qual será a distância da viagem em km? '))

if 200 >= d >= 0:
    kmCurto = 0.5
    preco = d * kmCurto
    print('O valor de cada km será de R${}'.format(kmCurto))
    print('O custo da viagem será de R${:.2f}'.format(preco))
if d > 200:
    kmLongo = 0.45
    preco = d * kmLongo
    print('O valor de cada km será de R${}'.format(kmLongo))
    print('O custo da viagem será de R${:.2f}'.format(preco))
if d < 0:
    print('{} é um número inválido.'.format(d))
