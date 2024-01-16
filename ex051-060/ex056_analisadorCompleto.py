somaIdade = 0
maiorIdadeHomem = 0
homemMaisVelho = ''

mulheresMenores = 0

for p in range(1, 5):
    print('----------- {}ª PESSOA ------------'.format(p))
    nome = str(input('Nome: '.format(p))).strip()
    idade = int(input('Idade: '.format(p)))
    sexo = str(input('Sexo [M/F]: '.format(p))).strip()

    somaIdade += idade

    if p == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        homemMaisVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        homemMaisVelho = nome

    if sexo in 'Ff' and idade < 20:
        mulheresMenores += 1


# Descobrindo a media do grupo
media = somaIdade/4
print('-'*30)
print('A media de idade do grupo é {} anos'.format(media))
# Qual o nome do homem mais velho
print('O homem mais velho é o {}, com {} anos'.format(homemMaisVelho, maiorIdadeHomem))
print('{} mulheres tem menos de 20 anos'.format(mulheresMenores))


