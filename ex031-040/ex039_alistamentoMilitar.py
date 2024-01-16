from datetime import date

ano = int(input('Digite seu ano de nascimento: '))
anoAtual = date.today().year

idade = anoAtual - ano
print('Você tem {} anos'.format(idade))

if idade < 18:
    idadeFalta = 18 - idade
    print('Faltam {} anos para seu alistamento!({})'.format(idadeFalta, ano+18))
elif idade == 18:
    print('Você está na idade para se alistar!')
elif idade > 18:
    idadePassou = idade - 18
    print('Você está {} ano(s) atrasado no alistamento!({})'.format(idadePassou, ano+18))
