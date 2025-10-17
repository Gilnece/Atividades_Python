'''Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço
da passagem, cobrando 0,50 por KM para viagens de até 200Km e 0,45 para viagens mais longas.'''

dis = float(input('Quantos Km tem sua viagem: '))

if dis <= 200:
    viagem = dis * 0.5
    print('O valor da viagem ficou em {:.2f}R$' .format(viagem))
if dis > 200:
    viagem = dis * 0.45
    print('O valor da viagem ficou em {:.2f}R$}'.format(viagem))
