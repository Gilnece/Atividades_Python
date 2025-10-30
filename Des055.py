'''criar script, que informe se um cliente tem desconto especial
20% sua compra tem que ser maior que 200R$ ou ser vip
se o valor total estiver entre 150 e 200 ele vai receber apenas 10%'''
from random import randint
vips = ['kleber', 'moises']
cliente = input('Informe o seu nome de cadastro: ')

compra = float(randint(1, 500))

if cliente in vips:
    if compra >= 200:
        desconto = compra - (compra * (20 / 100))
        print('Sua compra de R${:.2f} ficou com 20% de desconto!, ficando em R${:.2f}'.format(compra, desconto))
    elif 150 <= compra < 200:
        desconto = compra - (compra * (15 / 100))
        print('Sua compra de R${:.2f} ficou com 20% de desconto!, ficando em R${:.2f}'.format(compra, desconto))
    else:
        print('Sua compra não teve desconto, totalizando em R${:.2f}'.format(compra))
else:
    print('cliente não faz parte da lista VIP, compra sem desconto.')
    print('Total da compra: R${:.2f}'.format(compra))
