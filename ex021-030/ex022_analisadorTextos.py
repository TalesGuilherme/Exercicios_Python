nome = str(input('Digite o seu nome completo: ')).strip()

print('Analisando seu nome...')
print('O nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('O nome com todas as letras minúsculas: {}'.format(nome.lower()))
print('A quantidade de letras (sem espaços) é: {}'.format(len(nome)-nome.count(' ')))
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))

