from random import choice

a1 = input('Digite o nome do(a) primeiro(a) aluno(a): ')
a2 = input('Digite o nome do(a) segundo(a) aluno(a): ')
a3 = input('Digite o nome do(a) terceiro(a) aluno(a): ')
a4 = input('Digite o nome do(a) quarto(a) aluno(a): ')

lista = [a1, a2, a3, a4]
sorteador = choice(lista)

print('O aluno escolhido foi {}!'.format(sorteador))

