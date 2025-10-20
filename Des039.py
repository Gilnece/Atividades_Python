'''a confederação nacional de natação precisa de um
programa que leia o ano de nascimento de um atleta e
mostre sua categoria de com a idade
até 9 anos: mirim
até 14: infantil
19 junior
20 senior
acima master'''
import time
from datetime import date
from time import sleep

dia = date.today().day
mes = date.today().month
ano = date.today().year

print ('Levando em consideração a data: {}/{}/{}'.format(dia, mes, ano))
ano_nasc = int(input('Digite o ano de nascimento: '))

ano_atleta = ano - ano_nasc

print('\033[1;31mPROCESSANDO...\033[0m')
sleep(1)

if ano_atleta < 9:
    print('Com {} anos, é um atleta Mirim'.format(ano_atleta))
elif 9 < ano_atleta < 14:
    print('Com {} anos, é um atleta Infantil'.format(ano_atleta))
elif 14 < ano_atleta < 19:
    print('Com {}, é um atleta Junior'.format(ano_atleta))
elif 19 < ano_atleta < 20:
    print('Com {}, é um atleta Senior'.format(ano_atleta))
elif 20 < ano_atleta:
    print('com {} anos, é um atleta Master'.format(ano_atleta))