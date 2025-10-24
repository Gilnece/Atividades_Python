'''faça um programa que leia o peso de cinco pessoas. No final,
mostre qual foi o maior e o menor peso lidos'''

p = int(input('Quantas pessoas gostaria de analisar? '))
# inicializando
pesos = [] # cria uma lista para receber os pesos que seram informados posteriormente
for c in range(1, p+1): # for para informar os pesos
    peso = float(input('Digite o peso: '))
    pesos.append(peso) # anexa os pesos a lista
    maior = pesos[0] # atribui o peso maior a variavel maior
    menor = pesos[0] # atribui o peso menor a variavel menor
for peso in pesos: # compara os pesos informados, a lista que recebeu os pesos
    if peso > maior: # se o peso informado for o maior contido dentro da lista
        maior = peso # a variavel maior, irá receber o maior valor da lista
    elif peso < menor: # se o peso informado for o menor contido dentro da lista
        menor = peso # a variavel menor, irá receber o menor valor da lista
print('O menor peso é {}Kg'.format(menor))
print('O maior peso é {}Kg'.format(maior))
