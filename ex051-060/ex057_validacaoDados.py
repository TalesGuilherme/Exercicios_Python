sexo = ''
sexoPessoa = ''

while not sexo.upper() == 'M' and not sexo.upper() == 'F':
    sexo = str(input('Digite o seu sexo: [M/F] ')).strip()

    if sexo in 'Mm':
        sexoPessoa = 'Masculino'
    if sexo in 'Ff':
        sexoPessoa = 'Feminino'
    if sexo.upper() != 'M' and sexo.upper() != 'F':
        print('Entrada inválida. Digite novamente!')

print('Seu sexo é {}'.format(sexoPessoa))
