'''Escreva um programa que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu'''

import random
from time import sleep
print('-=-'*23)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar o computador...')
print('-=-'*23)
computador = random.randint(0,5)
escolha = int(input('tente adivinhar: '))
print('PROCESSANDO...')
sleep(2)
if escolha == computador:
    print('Parabéns você acertou!')
else:
    print('Hahaha eu ganhei')
    print('pensei no numero {}, mais sorte na proxima'.format(computador))
