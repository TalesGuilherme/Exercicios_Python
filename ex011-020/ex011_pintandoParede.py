largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura

print('A parede tem a dimensão de {}x{} e sua área é de {:.2f}m²!'.format(largura, altura, area))
qtdTinta = float(input('Quantos m² um litro de tinta pode pintar? '))

quantidadeTinta = area / qtdTinta

print('Será necessário utilizar {:.2f}l de tinta para pintar a parede!'.format(quantidadeTinta))
