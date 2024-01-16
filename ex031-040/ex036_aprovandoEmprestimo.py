vcasa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o sálario do comprador: R$'))
anos = float(input('Em quantos anos o comprador vai pagar? '))

prestacao = vcasa / (anos * 12)
exced = salario * (30/100)
print('Prestação mensal: R${:.2f}'.format(prestacao))

if prestacao <= exced:
    print('O empréstimo foi aprovado!')
elif prestacao > exced:
    print('O empréstimo não foi aprovado!')









