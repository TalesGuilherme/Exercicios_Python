from math import sin, cos, tan, radians

angulo = float(input('Digite o angulo que você deseja: '))
sin = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))

print('O angulo de {:.1f} tem o SENO de {:.2f}'.format(angulo, sin))
print('O angulo de {:.1f} tem o COSSENO de {:.2f}'.format(angulo, cos))
print('O angulo de {:.1f} tem a TANGENTE de {:.2f}'.format(angulo, tan))
