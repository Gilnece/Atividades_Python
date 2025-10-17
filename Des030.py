'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto'''
ano = int(input('Digite o ano desejado: '))
if ano % 4 == 0:
    print('o ano {} é bissexto'.format(ano))
else:
    print('o ano {} não é bissexto'.format(ano))
