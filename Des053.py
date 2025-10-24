'''faça um programa que leia o peso de cinco pessoas. No final,
mostre qual foi o maior e o menor peso lidos'''

p = int(input('Quantas pessoas gostaria de analisar? '))
if p <= 0:
    print('Nenhuma pessoa para analisar!') # adicionada validação para quando o usuario informar um total de zero pessoas para serem analisadas
else:
    # inicializando
    pesos = [] # cria uma lista para receber os pesos que seram informados posteriormente
    for c in range(p): # for para informar os pesos
        peso = float(input('Digite o peso: '))
        pesos.append(peso) # anexa os pesos a lista
    maior = pesos[0] # atribui o peso maior a variavel maior  / removido de dentro do laço for para que não se repita a interação diversas vezes
    menor = pesos[0] # atribui o peso menor a variavel menor  / removido de dentro do laço for para que não se repita a interação diversas vezes
    for peso in pesos: # compara os pesos informados, a lista que recebeu os pesos
        if peso > maior: # se o peso informado for o maior contido dentro da lista
            maior = peso # a variavel maior, irá receber o maior valor da lista
        elif peso < menor: # se o peso informado for o menor contido dentro da lista
            menor = peso # a variavel menor, irá receber o menor valor da lista
    print('O menor peso é {}Kg'.format(menor))
    print('O maior peso é {}Kg'.format(maior))
