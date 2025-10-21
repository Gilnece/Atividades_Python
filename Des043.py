'''crie um programa que faça o computador jogar jokenpô com você'''
import random
from time import sleep

print('-=-' * 23)
print('Jo - Ken - Pô')
print('-=-' * 23)

opcoes = ['pedra', 'papel', 'tesoura']

computador = random.choice(opcoes)
escolha = input('Vamos,tente acertar e ganhar de mim!\n ')
print('PROCESSANDO...')
sleep(2)
if computador == escolha:
    print('Vamos novamente! Escolhemos {}'.format(computador))
elif computador == 'pedra' and escolha == 'tesoura':
    print('Muito bem, você ganhou')
    print('{} ganha de {}'.format(computador, escolha))
elif computador == 'papel' and escolha == 'pedra':
    print('Muito bem, você ganhou')
    print('{} ganha de {}'.format(computador, escolha))
elif computador == 'tesoura' and escolha == 'papel':
    print('Muito bem, você ganhou')
    print('{} ganha de {}'.format(computador, escolha))

elif computador == 'tesoura' and escolha == 'pedra':
    print('mais sorte na proxima, eu ganhei, escolhi{}'.format(computador))
    print('{} ganha de {}'.format(computador, escolha))
elif computador == 'pedra' and escolha == 'papel':
    print('mais sorte na proxima, eu ganhei, escolhi{}'.format(computador))
    print('{} ganha de {}'.format(computador, escolha))
elif computador == 'papel' and escolha == 'tesoura':
    print('mais sorte na proxima, eu ganhei, escolhi{}'.format(computador))
    print('{} ganha de {}'.format(computador, escolha))
