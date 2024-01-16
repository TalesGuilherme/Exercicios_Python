from emoji import emojize

dias = int(input('Quantos dias o carro foi alugado? '))
print('\n', '-'*7, 'ATENÇÃO: Utilizar "." em caso de número decimal!', '-'*7)
km = float(input('\nQuantos quilômetros rodados? '))

precoDia = float(input('Qual é o valor da diária do carro? R$'))
precoKm = float(input('Qual é o valor do Km rodado? R$'))

diasCalculo = dias * precoDia
kmCalculo = km * precoKm
total = diasCalculo + kmCalculo

print('O total a pagar é de R${:.2f}!'.format(total), '\n')

print('Obrigado por adquirir nossos serviços!', emojize(":sunglasses:", language='alias'))
