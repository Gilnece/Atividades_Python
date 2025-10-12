# faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
#cosseno e tangente desse ângulo

from math import sin, cos, tan
angulo = float(input('Digite um angulo: '))
seno = sin(angulo)
coseno = cos(angulo)
tangente = tan(angulo)
print('Para o angulo {:.0f}º temos seno={} coseno={} e tangente={}'.format(angulo, seno, coseno, tangente))