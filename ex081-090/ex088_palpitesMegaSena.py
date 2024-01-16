from random import randint
from time import sleep

palpites = list()
jogos = int(input('Quantos jogos serão criados? '))

while not jogos == 0:
    palpite = [[randint(1, 60)], [randint(1, 60)], [randint(1, 60)], [randint(1, 60)], [randint(1, 60)], [randint(1, 60)]]

    # Verificando se há algum elemento repetido em "palpite"
    for pos, numero in enumerate(palpite):
        if numero in palpite[pos + 1:]:
            while numero in palpite[pos + 1]:
                palpite = [[randint(1, 60)], [randint(1, 60)], [randint(1, 60)], [randint(1, 60)], [randint(1, 60)],
                           [randint(1, 60)]]

    palpite.sort()
    palpites.append(palpite[:])
    palpite.clear()
    jogos -= 1

print('-'*35)
print(f'\033[32mOs jogos criados foram: \033[m')
for pos, jogo in enumerate(palpites):
    sleep(0.3)
    if pos == 0:
        print(f'{pos+1}° jogo: ', end='')
    else:
        print('\n'f'{pos+1}° jogo: ', end='')
    for n in jogo:
        print(f'{n}', end='')

print('\n'f'{"< BOA SORTE! >":-^35}')
