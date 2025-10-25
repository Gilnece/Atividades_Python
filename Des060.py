'''faça um programa que leia um numero qualquer e mostre o seu fatorial
ex:  5! = 5x4x3x2x1 = 120'''

from math import factorial

num = int(input('Digite um numero: '))
while num > 1:
    print('{}! = {}'.format(num, factorial(num)))
    break

'''n = int(input("Digite um número para calcular o fatorial: "))
f = 1
contador = n
while contador > 0:
    f *= contador
    contador -= 1
print(f"O fatorial de {n} é {f}")'''