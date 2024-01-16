nome = str(input('Qual é o seu nome completo? ')).strip()

nome = nome.upper()
nome = nome.split()

print('Seu nome tem Silva? {}'.format('SILVA' in nome))
