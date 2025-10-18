'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre
uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,99 oir casa KM acima do limite.'''

from random import randint

print('Velocidade permitida: 80KM/h')
velocidade = randint(1, 300) #subtendendo que a velocidade seja registrada em uma lombada eletronica
multa = (velocidade - 80) * 7.99

if velocidade > 80:
    print('Você está sendo multado por conduzir acima da velocidade permitida')
    print('Velocidade maxima permitida: 80KM/h')
    print('Velocidade registrada: {}'.format(velocidade))
    print('Valor da multa: {:.2f}R$'.format(multa))
else:
    print('Velocidade registrada: {}'.format(velocidade))
    print('Otima condução, cuidado na estrada!')
