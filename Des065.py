'''crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre
a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar
ao usuário se ele quer ou não continuar a digitar valores.'''

soma = 0
quant = 0
media = 0
resposta = ''

while True:
    num = int(input('Digite um numero: '))
    if num == num:
        resposta = str(input('deseja continuar(sim/não): '))
        if resposta == 'sim':
            soma += num
            quant += 1
        else:
            soma += num
            quant += 1
            media = soma / quant
            break
print('Você digitou {} números e a media entre eles foi {}.'.format(quant, media))