from datetime import date
from time import sleep

atingiram = 0
naoAtingiram = 0
invalidos = 0
anoAtual = date.today().year

print('Digite o ano de nascimento de 7 pessoas, para saber quantas são maiores e(ou) menores de idade')
print('='*100)

for pess in range(1, 8):

    ano = int(input('\n\033[mEm que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = anoAtual - ano

    if ano < 0 or ano >= anoAtual or idade > 100:
        print('\033[31mAno inválido!')
        invalidos += 1
    elif 21 > idade > 0:
        print('\033[32mA pessoa que nasceu em {} é menor de idade!'.format(ano))
        naoAtingiram += 1
    elif idade >= 21:
        print('\033[32mA pessoa que nasceu em {} é maior de idade!'.format(ano))
        atingiram += 1

for d in range(0, 40):
    sleep(0.1)
    print('\033[m=', end='')

print('\n{} pessoa(s) atingiram a maioridade!'.format(atingiram))
print('{} pessoa(s) ainda não atingiram a maioridade!'.format(naoAtingiram))
print('\033[31mTotal de dados inválidos: {}'.format(invalidos))
