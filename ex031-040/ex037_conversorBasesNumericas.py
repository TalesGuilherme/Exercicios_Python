n = int(input('Digite um número inteiro qualquer: '))
base = int(input("""Escolha qual será a base de conversão: 
[1] BINARIO
[2] OCTAL
[3] HEXADECIMAL
Digite aqui: """))

if base == 1:
    print('{} convertido para Binário é igual a {}'.format(n, bin(n)[2:]))
elif base == 2:
    print('{} convertido para Octal é igual a {}'.format(n, oct(n)[2:]))
elif base == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida! Tente novamente')
