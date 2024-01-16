salarioAtual = float(input('Digite o salário atual do funcionário: '))
reajuste = float(input('Digite a porcentagem do reajuste(sem o sinal de "%"): '))
reajusteCalculo = salarioAtual * (reajuste/100)
novoSalario = salarioAtual + reajusteCalculo

print('O valor a ser acrescentado ao salário (reajuste) é R${:.2f}'.format(reajusteCalculo))
print('O novo salário do funcionário, já com o reajuste: R${:.2f}'.format(novoSalario))
