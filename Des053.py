'''faça um programa que leia o peso de cinco pessoas. No final,
mostre qual foi o maior e o menor peso lidos'''

p = int(input('Quantas pessoas gostaria de analisar? '))
pesos = []
for c in range(0, p):
    peso = float(input('Digite o peso: '))
    pesos.append(peso) # adiciona o peso na lista
maior = pesos[0]
menor = pesos[0]
for peso in pesos:
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O menor peso é {}Kg'.format(menor))
print('O maior peso é {}Kg'.format(maior))