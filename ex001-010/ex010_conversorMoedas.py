real = float(input('Quantos reais você tem? R$'))
dolar = 4.86
euro = 5.27
convertDolar = real / dolar
convertEuro = real / euro

print('Com R${:.2f}, é possível comprar U${:.2f}'.format(real, convertDolar))
print('Com R${:.2f}, é possível comprar {:.2f} euros'.format(real, convertEuro))
