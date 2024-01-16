n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
soma = 0
sub = 0
mult = 0
comando = 0

while not comando == 6:

    print("""\nLista de comandos:
[1] SOMA
[2] SUBTRAÇÃO
[3] MULTIPLICAÇÃO
[4] MAIOR
[5] DIGITAR NOVOS NÚMEROS
[6] SAIR DO PROGRAMA""")
    comando = int(input('\nDigite o comando[1/5]: '))

    # [1] COMANDO DE SOMA
    if comando == 1:
        soma = n1 + n2
        print('-'*30)
        print('A soma de {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, soma))

    # [2] COMANDO DE SUBTRAÇÃO
    if comando == 2:
        sub = n1 - n2
        print('-'*30)
        print('A subtração entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, sub))

    # [3] COMANDO DE MULTIPLICAÇÃO
    if comando == 3:
        mult = n1 * n2
        print('-'*30)
        print('A multiplicação entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, mult))

    # [4] COMANDO PARA SABER QUAL É O MAIOR E O MENOR
    if comando == 4:
        print('-' * 30)
        if n1 > n2:
            print('O maior é {:.1f} e o menor é {:.1f}'.format(n1, n2))
        elif n2 > n1:
            print('O maior é {:.1f} e o menor é {:.1f}'.format(n2, n1))
        else:
            print('Os dois valores são iguais!')

    # [5] COMANDO PARA DIGITAR NOVOS VALORES PARA O PRIMEIRO E O SEGUNDO
    if comando == 5:
        print('-' * 30)
        n1 = float(input('Digite um novo valor para o primeiro: '))
        n2 = float(input('Digite um novo valor para o segundo: '))

    if comando > 6 or comando < 1:
        print('Entrada inválida!')

print('O programa foi encerrado.')
