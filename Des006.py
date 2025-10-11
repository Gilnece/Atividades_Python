# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

#já que 1 metro tem 100 cm e 1000 milimetros, vou me basear nesses valores para fazer os calculos

num = float(input('Digite quantos metros deseja converter: '))

cent = num * 100
mili = num * 1000

print('{} metros são {:.0f}cm'.format(num, cent))
print('{} metros são {:.0f}mm'.format(num, mili))