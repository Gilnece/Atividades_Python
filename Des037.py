'''faça um programa que leia o ano de nascimento de um jovem
e informe, de acordo com sua idade:
se ele ainda vai se alistar ao serviço militar
se é a hora de se alistar
se já passou do tempo de alistamento

seu programa também deverá mostrar o tempo que falta ou que passou do prazo'''

#idade minima para para se alistar é de 18 anos
#idade maxima para se alistar é de 45 anos

from datetime import date

ano = int(input('Qual o ano que nasceu: '))
atual = date.today().year
data = atual - ano
if data == 18:
    print('esta na hora de se alistar')
    print('vocês está com {} anos'.format(data))
elif data < 18:
    print('está quase na hora')
    quase = (data - 18) * (-1)
    #positivo = quase * (-1)
    print('falta {} anos para se alistar'.format(quase))
elif data <= 45:
    print('Idade maxima para alistamento é de 45 anos, você tem {} anos, ainda está na hora de se alistar'.format(data))
elif data >= 45:
    passou = data - 45
    if passou > 1:
        print('Ops! Você está com {} anos,já passaram {} anos que deveria ter se alistado'.format(data,passou))
    else:
        print('Ops! Você está com {},já passou {} ano que deveria ter se alistado'.format(data, passou))