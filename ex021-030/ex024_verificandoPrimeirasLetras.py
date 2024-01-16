print('Verificando se você nasceu em uma cidade que tem "Santo" como primeiro nome!\n')
cidade = str(input('Em que cidade você nasceu? ')).strip()

print('\n''Você nasceu em uma cidade que tem "SANTO" como primeiro nome? {}'.format(cidade[:5].upper() == 'SANTO'))
