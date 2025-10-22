'''crie um programa que faça o computador jogar jokenpô com você'''
import random
from time import sleep

print('-=-' * 23)
print('Jo - Ken - Pô')
print('-=-' * 23)

opcoes = ['pedra', 'papel', 'tesoura']

computador = random.choice(opcoes)
escolha = input('Vamos,tente acertar e ganhar de mim: ')
print('PROCESSANDO...')
sleep(1)
if computador == escolha:
    print('Vamos novamente! Escolhemos {}'.format(computador))
elif computador == 'pedra' and escolha == 'tesoura':
    print('mais sorte na proxima')
    print('{} ganha de {}'.format(computador, escolha))
elif computador == 'papel' and escolha == 'pedra':
    print('mais sorte na proxima')
    print('{} ganha de {}'.format(computador, escolha))
elif computador == 'tesoura' and escolha == 'papel':
    print('mais sorte na proxima')
    print('{} ganha de {}'.format(computador, escolha))

elif computador == 'tesoura' and escolha == 'pedra':
    print('muito bem você ganhou, escolhi {}'.format(computador))
    print('{} perde de {}'.format(computador, escolha))
elif computador == 'pedra' and escolha == 'papel':
    print('muito bem você ganhou, escolhi {}'.format(computador))
    print('{} perde de {}'.format(computador, escolha))
elif computador == 'papel' and escolha == 'tesoura':
    print('muito bem você ganhou, escolhi {}'.format(computador))
    print('{} perde de {}'.format(computador, escolha))
elif escolha != 'pedra' and escolha != 'tesoura' and escolha != 'papel':
    print('Deixa de ser burro e escolhe certo!')
