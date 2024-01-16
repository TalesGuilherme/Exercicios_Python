tabela = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'RB Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco da Gama', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')

print('\nA tabela final do Brasileirão 2023\n')
for pos, colocacao in enumerate(tabela):
    print(f'{pos+1}° {colocacao}')

print('\n\033[32mOs 5 primeiros colocados são:\033[m')
for pos, colocacao in enumerate(tabela[:5]):
    print(colocacao)

print('\n\033[31mOs 4 últimos colocados são:\033[m')
for pos, colocacao in enumerate(tabela[16:21]):
    print(colocacao)

print('\n\033[33mOs times em ordem alfabética:\033[m')
for pos, colocacao in enumerate(sorted(tabela)):
    print(colocacao)

print(f'\n\033[35mO Santos está na posição 17ª\033[m')
