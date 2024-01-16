from math import hypot

catOposto = float(input('Digite o valor do cateto oposto: '))
catAdja = float(input('Digite o valor do cateto adjascente: '))
hipotenusa = hypot(catOposto, catAdja)

print('O valor da hipotenusa é {:.2f}!'.format(hipotenusa))
