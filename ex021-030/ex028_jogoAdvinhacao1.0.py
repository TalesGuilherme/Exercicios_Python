from random import randint
from time import sleep
from emoji import emojize
import pygame
pygame.init()

pygame.mixer.music.load('ex028.mp3')
pygame.mixer.music.play(loops=3)
input()
pygame.event.wait()

n = randint(0, 5) # Sorteio de números
print("""Olá! Seja bem-vindo(a) ao "Advinhe o número!".
\nNeste jogo, o desafio é adivinhar em qual número eu estou pensando...""")

palpite = int(input('Digite um número inteiro entre 0 e 5: \n')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if palpite == n:
    print('\nVocê acertou! Realmente você é bom nesse jogo...', end='')
    print(emojize(":sunglasses:", language='alias'))
else:
    print('\nERRROOOOUUU KKKK\n')
    print('O número que eu pensei foi {}'.format(n), end='')
    print(emojize(":rolling_on_the_floor_laughing:", language='alias'))

print('Obrigado por participar, até a próxima!')
