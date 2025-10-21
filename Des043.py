'''crie um programa que faça o computador jogar jokenpô com você'''
from random import choice
from time import sleep

print('-=-' * 23)
print('Jo - Ken - Pô')
print('-=-' * 23)

opcoes = ['pedra', 'papel', 'tesoura']

computador = choice(opcoes)
escolha = input('Vamos,tente acertar e ganhar de mim!\n ')
print('PROCESSANDO...')
sleep(2)
if computador == escolha:
    print('Vamos novamente! Escolhemos {}'.format(computador))
elif computador == 'pedra' and escolha == 'tesoura':
    print('Mais sorte na proxima, eu ganhei')
    print('{} perde de {}'.format(escolha, computador))
elif computador == 'papel' and escolha == 'pedra':
    print('Mais sorte na proxima, eu ganhei')
    print('{} perde de {}'.format(escolha, computador))
elif computador == 'tesoura' and escolha == 'papel':
    print('Mais sorte na proxima, eu ganhei')
    print('{} perde de {}'.format(escolha, computador))

elif computador == 'tesoura' and escolha == 'pedra':
    print('Muito bem, Você ganhou, escolhi {}'.format(computador))
    print('{} ganha de {}'.format(escolha, computador))
elif computador == 'pedra' and escolha == 'papel':
    print('Muito bem, Você ganhou, escolhi {}'.format(computador))
    print('{} ganha de {}'.format(escolha, computador))
elif computador == 'papel' and escolha == 'tesoura':
    print('Muito bem, Você ganhou, escolhi {}'.format(computador))
    print('{} ganha de {}'.format(escolha, computador))

