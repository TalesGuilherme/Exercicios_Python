print('\nDigite três valores e vou dizer qual é o MAIOR e qual é o MENOR!\n')
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))

# Casos do n1 ===============================================
if n1 > n2 > n3:
    print('\nMAIOR: {:.1f}\nMENOR: {:.1f}'.format(n1, n3))
if n1 > n3 > n2:
    print('\nMAIOR: {:.1f}\nMENOR: {:.1f}'.format(n1, n2))

# Casos do n2 ===============================================
if n2 > n1 > n3:
    print('\nMAIOR: {:.1f}\nMENOR: {:.1f}'.format(n2, n3))
if n2 > n3 > n1:
    print('\nMAIOR: {:.1f}\nMENOR: {:.1f}'.format(n2, n1))

# Casos do n3 ===============================================
if n3 > n2 > n1:
    print('\nMAIOR: {:.1f}\nMENOR: {:.1f}'.format(n3, n1))
if n3 > n1 > n2:
    print('\nMAIOR: {:.1f}\nMENOR: {:.1f}'.format(n3, n2))

# Casos de igualdade MAIOR DE 2
if n1 == n2 > n3:
    print('\nMAIOR: {:.1f}\nMENOR: {:.1f}'.format(n1, n3))
if n2 == n3 > n1:
    print('\nMAIOR: {:.1f}\nMENOR: {:.1f}'.format(n2, n1))
if n1 == n3 > n2:
    print('\nMAIOR: {:.1f}\nMENOR: {:.1f}'.format(n1, n2))

# Casos de igualdade MENOR DE 2
if n1 > n2 == n3:
    print('\nMAIOR: {:.1f}\nMENOR: {:.1f}'.format(n1, n2))
if n2 > n1 == n3:
    print('\nMAIOR: {:.1f}\nMENOR: {:.1f}'.format(n2, n1))
if n3 > n2 == n1:
    print('\nMAIOR: {:.1f}\nMENOR: {:.1f}'.format(n3, n2))

# Caso todos sejam iguais
if n1 == n2 == n3:
    print('\nTodos os números são iguais.')
