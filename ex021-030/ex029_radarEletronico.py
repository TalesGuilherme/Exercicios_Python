vel = float(input('Digite a velocidade do carro (em km): '))

if vel > 80:
    multa = (vel-80) * 7
    print('\n{}km/h não é permitido! Você foi multado!'.format(vel))
    print('O valor da multa é R${:.1f}'.format(multa))

print('\n{}km/h está dentro do limite. Você não será multado.'.format(vel))
print('\nLembre-se de sempre utilizar o cinto de segurança e de respeitar os limites de velocidade!')





