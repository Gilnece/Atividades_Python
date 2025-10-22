'''Faça um programa que leia um número inteiro e diga se ele é ou não
um número primo'''

num = int(input('Digite um numero inteiro: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0: # quando o numero for divisivel pela razão
        print('\033[34m', end='')
        tot += 1
    else: # quando o numero não for divisivel pela razão
        print('\033[31m', end='')
    print('{} '.format(c), end=' ')
print('\nO numero {} foi divisivel {} vezes'.format(num, tot))
print('Os numeros pintados de azul são os divisores')
if tot == 2:
    print('Por isso ele é primo')
else:
    print('Por isso ele não é primo')
#um numero primo é um numero que é divisivel por ele mesmo ou por 1