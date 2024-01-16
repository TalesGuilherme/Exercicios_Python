n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2
print('A media do aluno foi: {:.1f}'.format(media))
if n1 < 0 or n2 < 0 or media > 10:
    print('\033[31mVocê digitou algum valor inválido')
elif media < 5.0:
    print('\033[31mALUNO REPROVADO')
elif 6.9 >= media > 5.0:
    print('\033[33mALUNO EM RECUPERAÇÃO')
elif media >= 7.0:
    print('\033[32mALUNO APROVADO')

