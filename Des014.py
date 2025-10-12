#crie um programa que leia um número Real qualquer pelo teclado e mostre na
#tela a sua porção inteira. Ex: Digite um numero 6.127 o numero 6.127 tem a parte inteira 6
import math

inteiro = float(input('Digite um valor com fracionado: '))

print('O valor inteiro de {} é {}'.format(inteiro, math.trunc(inteiro)))
