from time import sleep

preco = float(input('\033[35mDigite o preço do produto: R$'))
formaPagamento = int(input("""\n\033[36mDigite a forma de Pagamento: 
[1] - À vista Dinheiro/Cheque (10% desconto)
[2] - À vista no Cartão
[3] - 2x no Cartão
[4] - 3x no Cartão (juros de 20%)
\n\033[32mDigite aqui o número correspondente à forma escolhida: """))

vista = preco - (preco * (10/100))
vistaCartao = preco - (preco * (5/100))
cartao2x = preco / 2

# Pagamento a vista no Dinheiro/Cheque
if formaPagamento == 1:
    print('\nDesconto de 10% em vigor...')
    print('PROCESSANDO...')
    sleep(2)
    print('Valor a pagar: R${:.2f}'.format(vista))
# Pagamento a vista no Cartão
elif formaPagamento == 2:
    print('\nDesconto de 5% em vigor...')
    print('PROCESSANDO...')
    sleep(2)
    print('Valor a pagar: R${:.2f}'.format(vistaCartao))
# Pagamento parcelado em 2x no Cartão
elif formaPagamento == 3:
    print('PROCESSANDO...')
    sleep(2)
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros.'.format(cartao2x, cartao2x))
# Pagamento parcelado em 3x no Cartão com juros de 20%
elif formaPagamento == 4:
    vezes = int(input('Em quantas vezes será parcelado? '))
    cartao3x = (preco + (preco * (20 / 100))) / vezes
    print('Juros de 20% em vigor...')
    print('PROCESSANDO...')
    sleep(2)
    print('Sua compra será parcelada em 10x de R${:.2f} com um juros de 20%.'.format(cartao3x))
elif formaPagamento > 4 or formaPagamento <= 0:
    print('\033[31mForma de pagamento inválida! Digite uma das funções apresentadas.')

print('\n\033[32mObrigado por adquirir nossos produtos!')
