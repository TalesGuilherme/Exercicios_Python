produto = float(input('Digite o preço do produto: R$'))
desconto = float(input('Digite a porcentagem do desconto: '))
descontoCalculo = produto * (desconto/100)
novoPreco = produto - descontoCalculo

print('O desconto sobre esse produto é de R${:.2f}!'.format(descontoCalculo))
print('O novo preço do produto é R${:.2f}'.format(novoPreco))
