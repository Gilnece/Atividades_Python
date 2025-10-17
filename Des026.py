'''Escreva um programa que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu'''

import random
computador = random.randint(0,5)
escolha = int(input('Digite um numero entre 0 e 5: '))

if escolha == computador:
    print('Parabéns você acertou!')
else:
    print('Tente novamente na proxima')
