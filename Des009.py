# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
#quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

lar = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))

area = lar * alt
tinta = area / 2

print('A area da parede é: {:.3f}m²'.format(area))
print('Vai precisar de {:.2f}l de tinta'.format(tinta))