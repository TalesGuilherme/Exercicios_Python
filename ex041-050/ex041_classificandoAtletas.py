from datetime import date
ano = int(input('\033[34mDigite o ano de nascimento do atleta: \033[34m'))

anoAtual = date.today().year
idade = anoAtual - ano
print('\n\033[32mA idade do atleta é {} anos\033[32m'.format(idade))
if idade <= 9:
    print('\033[36mCategoria: MIRIM(até 9 anos)')
elif 14 >= idade > 9:
    print('\033[36mCategoria: INFANTIL(até 14 anos)')
elif 19 >= idade > 14:
    print('\033[36mCategoria: JUNIOR(até 19 anos)')
elif 20 >= idade > 19:
    print('\033[36mCategoria: SÊNIOR(até 20 anos)')
elif idade > 20:
    print('\033[36mCategoria: MASTER(acima de 20)')
