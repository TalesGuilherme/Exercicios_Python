numeros = list()

for c in range(0, 5):
    n = int(input('Digite um número inteiro: '))
    # Caso seja o primeiro valor
    if c == 0 or n > numeros[-1]:
        numeros.append(n)
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                break
            pos += 1
print('-'*30)
print(f'Os valores da lista ordenada são: {numeros}')







