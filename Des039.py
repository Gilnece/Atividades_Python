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

ano = date.today().year

print ('Levando em consideração a data: {}/{}/{}'.format(dia, mes, ano))
ano_nasc = int(input('Digite o ano de nascimento: '))
ano_atleta = ano - ano_nasc
print('\033[1;31mPROCESSANDO...\033[0m')
sleep(1)

if ano_atleta <= 9:
    print('Com {} anos, é um atleta Mirim'.format(ano_atleta))
elif ano_atleta <= 14:
    print('Com {} anos, é um atleta Infantil'.format(ano_atleta))
elif ano_atleta <= 19:
    print('Com {}, é um atleta Junior'.format(ano_atleta))
elif ano_atleta <= 25:
    print('Com {}, é um atleta Senior'.format(ano_atleta))
else:
    print('com {} anos, é um atleta Master'.format(ano_atleta))
