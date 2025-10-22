'''desenvolva um programa que leia o primeiro termo e a razão de um PA.
No final, mostre os 10 primeiros termos dessa progressão'''
#PA - progressão aritmetica

a1 = int(input('primeiro  termo: '))
r = int(input('Razão: '))
dez = a1 + (10 - 1) * r

for pa in range(a1, dez + r, r):
    print('{}'.format(pa), end='➜ ')
print('FIM')

