from emoji import emojize

n = str(input('Digite o seu nome completo: ')).strip()
print('É um prazer conhecê-lo(a) {}!'.format(n), end='')
print(emojize(":sunglasses:", language='alias'))

nome = n.split()

print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
