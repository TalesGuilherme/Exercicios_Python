print('Método para calcular o IMC (Índice de massa corporal)\n')
peso = float(input('Digite o peso(KG): '))
altura = float(input('Digite a altura(M): '))

imc = peso / (altura ** 2)
print('\nO seu IMC é {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso!')
elif 25 >= imc >= 18.5:
    print('Você está no peso ideal!')
elif 30 >= imc > 25:
    print('Você está com Sobrepeso!')
elif 40 >= imc > 30:
    print('Você está com Obesidade!')
elif imc > 40:
    print('Você está com Obesidade Mórbida!')
