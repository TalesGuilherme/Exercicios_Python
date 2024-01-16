s = float(input('Digite o salário do funcionário: R$'))

if s > 1250:
    aumento = 10
    print('O aumento será de {}%'.format(aumento))
    calculoAumento = s * aumento/100
    print('Será acrescentado ao salário atual R${:.2f}'.format(calculoAumento))
    reajuste = calculoAumento + s
    print('O novo salário do funcionário será R${:.2f}'.format(reajuste))
if 1250 >= s > 0:
    aumento = 15
    print('O aumento será de {}%'.format(aumento))
    calculoAumento = s * aumento/100
    print('Será acrescentado ao salário atual R${:.2f}'.format(calculoAumento))
    reajuste = calculoAumento + s
    print('O novo salário do funcionário será R${:.2f}'.format(reajuste))
if s <= 0:
    print('Valor inválido!')
