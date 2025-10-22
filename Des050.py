'''Faça um programa que leia um número inteiro e diga se ele é ou não
um número primo'''

'''para instalar a biblioteca foi usado o comando pip install sympy
from sympy import isprime, primerange, nextprime #importados os metodos necessarios para saber se um numero é primo ou não
Verifica se um número é primo
print(isprime(29))   # ✅ True
print(isprime(15))   # ❌ False
Gera todos os primos de um intervalo
primos = list(primerange(1, 50))
print(primos)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
Encontra o próximo número primo após X
print(nextprime(50))  # 53'''

from sympy import isprime, nextprime
num = int(input('Digite um numero inteiro: '))

if isprime(num):
    print('o numero {} é Primo'.format(num))
    print('o proximo numero primo é {}'.format(nextprime(num)))
else:
    print('o numero {} não é Primo'.format(num))