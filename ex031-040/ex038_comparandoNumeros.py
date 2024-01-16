print('\033[35mVamos verificar o maior entre dois números inteiros\033[35m\n')
n1 = int(input('\033[34mDigite o primeiro número inteiro: \033[34m'))
n2 = int(input('\033[34mDigite o segundo número inteiro: \033[34m'))

if n1 > n2:
    print('\033[31mO primeiro valor é maior!')
elif n2 > n1:
    print('\033[31mO segundo valor é maior!')
else:
    print('\033[31mOs dois valores são iguais.')


