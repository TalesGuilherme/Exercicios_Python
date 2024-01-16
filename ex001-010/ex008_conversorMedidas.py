n = float(input('Digite o valor em metros: '))
toKm = n / 1000
toHec = n / 100
toDecam = n / 10
toDecim = n * 10
toCent = n * 100
toMili = n * 1000

print('O valor de {} metros em quilômetros é {}km'.format(n, toKm))
print('O valor de {} metros em hectômetros é {}hm'.format(n, toHec))
print('O valor de {} metros em decâmetros é {}dam'.format(n, toDecam))
print('O valor de {} metros em decímetros é {:.0f}dm'.format(n, toDecim))
print('O valor de {} metros em centímetros é {:.0f}cm'.format(n, toCent))
print('O valor de {} metros em milímetros é {:.0f}mm'.format(n, toMili))
