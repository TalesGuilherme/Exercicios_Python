print('Digite o valor de três retas, para verificar se há a possibilidade de se formar um triângulo\n')
n1 = float(input('Digite o valor da primeira reta: '))
n2 = float(input('Digite o valor da segunda reta: '))
n3 = float(input('Digite o valor da terceira reta: '))

if n1+n2 > n3 and n1+n3 > n2 and n2+n3 > n1:
    print('Pode ser feito um triângulo!')
else:
    print('Não será possível fazer um triângulo...')
