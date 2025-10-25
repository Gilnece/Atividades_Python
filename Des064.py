'''Crie um programa que leia vários numeros inteiros pelo teclado. O programa só vai parar quando o
usúario digitar o valor 999, que é a condição de parada. No final mostre quantos números foram
digitados e qual foi a soma entre eles(desconsiderando o flag)'''

print('Digite 0(Zero), para parar!')
soma = 0
quant = 0

while True:
    num = int(input('Digite um numero: '))
    if num == 0:
        break
    soma += num
    quant += 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(quant, soma))