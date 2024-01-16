from random import randint
from time import sleep

print('Vamos jogar JOKENPÔ!')
print("""Suas Opções: 
[1] PEDRA
[2] PAPEL
[3] TESOURA""")
jogador = int(input('Qual é a sua jogada? '))
computador = randint(1, 3)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

# Opções que o JOGADOR VENCE ===========================
if jogador == 1 and computador == 3:
    print('=' * 15)
    print('JOGADOR VENCEU')
    print('=' * 15)
    print('Jogador escolheu Pedra')
    print('Computador escolheu Tesoura')
    print('=' * 15)
elif jogador == 2 and computador == 1:
    print('=' * 15)
    print('JOGADOR VENCEU')
    print('=' * 15)
    print('Jogador escolheu Papel')
    print('Computador escolheu Pedra')
    print('=' * 15)
elif jogador == 3 and computador == 2:
    print('=' * 15)
    print('JOGADOR VENCEU')
    print('=' * 15)
    print('Jogador escolheu Tesoura')
    print('Computador escolheu Papel')
    print('=' * 15)

# Opções que o COMPUTADOR VENCE =========================
if computador == 1 and jogador == 3:
    print('=' * 15)
    print('COMPUTADOR VENCEU')
    print('=' * 15)
    print('Computador escolheu Pedra')
    print('Jogador escolheu Tesoura')
    print('=' * 15)
elif computador == 2 and jogador == 1:
    print('=' * 15)
    print('COMPUTADOR VENCEU')
    print('=' * 15)
    print('Computador escolheu Papel')
    print('Jogador escolheu Pedra')
    print('=' * 15)
elif computador == 3 and jogador == 2:
    print('=' * 15)
    print('COMPUTADOR VENCEU')
    print('=' * 15)
    print('Computador escolheu Tesoura')
    print('Jogador escolheu Papel')
    print('=' * 15)

# Caso de EMPATE ===========================
elif jogador == computador:
    print('=' * 15)
    print('EMPATE')
    print('=' * 15)
