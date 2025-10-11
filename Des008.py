#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
#considerar o Dólar atual
#considerar o Dólar na data da aula US$1,00 = R$3.27

din = float(input('Quanto você tem: '))

dolar = (din / 3.27)
doratual = (din / 5.53)

print('com R${} você conseguia comprar U${:.4f} antes da pandemia'.format(din, dolar))
print('com R${} hoje você consegue comprar apenas U${:.4f}'.format(din, doratual))