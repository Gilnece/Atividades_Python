'''crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar'''

num = int(input('Digite um numero: '))
if num % 2 == 0:
    print('O numero {} é Par'.format(num))
else:
    print('O numero {} é Impar'.format(num))