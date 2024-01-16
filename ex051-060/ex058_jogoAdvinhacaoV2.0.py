from random import randint
from time import sleep

print('---------JOGO DA ADIVINHAÇÃO-----------')

for c in range(0, 39):
    sleep(0.1)
    print('.', end='')

print("""\n\nRegras:
- Digite um número de 1 a 10
- Quem fizer menos tentativas vence (é bom jogar contra um amigo)
- Será que você consegue acertar o número que estou pensando?""")
computador = randint(0, 10)
jogador = -1
tentativas = 1
while not jogador == computador:
    jogador = int(input('\nDigite um número inteiro: '))

    if jogador == computador:
        print('Parabéns, você acertou!')
    else:
        print('Você errou...')
        tentativas += 1

print('NÚMERO DE TENTATIVAS: {}'.format(tentativas))
