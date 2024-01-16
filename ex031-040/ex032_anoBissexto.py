from datetime import date

print('Analisando se um ano é BISSEXTO ou não. (Caso queira verificar o ano atual, digite "0")\n')
ano = int(input('Digite um ano para ser analisado: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é Bissexto!'.format(ano))
else:
    print('O ano de {} não é Bissexto...'.format(ano))
if ano < 0:
    print('Ano inválido!')
