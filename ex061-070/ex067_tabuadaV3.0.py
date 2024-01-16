n = 0
mult = 0

while True:
    n = int(input('\nDigite um número inteiro: '))
    print('-'*30)
    if n < 0:
        print('\033[31mO número digitado é inválido!')
        break
    else:
        while mult < 11:
            tab = n * mult
            print(f'{n} x {mult} = {tab}')
            mult += 1
            if mult == 11:
                mult = 0
                break
    print('-'*30)

print('A tabuada foi encerrada.\033[m')
print('-'*30)
