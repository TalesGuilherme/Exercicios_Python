f = str(input('Digite uma frase: ')).strip().upper()
palavras = f.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]

print('\033[34m{} ao contrário fica: {}'.format(junto, inverso))
if junto == inverso:
    print('\033[32mPortanto, {} é um palíndromo!'.format(junto))
else:
    print('\033[31mPortanto {} não é um palíndromo!'.format(junto))