frase = str(input('Digite uma frase: ')).strip()
print('Escolha uma letra para verificar: \n- Quantas vezes aparece na frase \n- Onde a primeira e última aparece na frase: ', end='')
letra = str(input(' ')).upper()

print('\nVocê escolheu a letra {}'.format(letra))
print('Analisando...')

frase = frase.upper()
print('\nA letra {} aparece {} vezes nessa frase.'.format(letra, frase.count(letra)))
print('A primeira letra {} apareceu na posição: {}'.format(letra, frase.find(letra)+1))
print('A última letra {} apareceu na posição: {}'.format(letra, frase.rfind(letra)+1))



