#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
#retângulo, calcule e mostre o comprimento da hipotenusa

import math

#catetoad = (float(input('Qual tamanho do cateto Adjacente:')))
#catetoop = (float(input('Qual tamanho do cateto oposto:')))
#formula de calculo para hipotenusa: a = raiz de b²+C²
#sendo b = cateto adjacente e c = cateto oposto
#hipotenusa = (((catetoad ** 2) + (catetoop ** 2)) ** (1/2))
#print('A hipotenusa entre os catetos {} e {} é {}'.format(catetoad, catetoop, hipotenusa))

cateto1 = float(input('Qual o valor do cateto adjacente: '))
cateto2 = float(input('Qual o valor do cateto oposto: '))
hipotenusa = math.sqrt((cateto1**2) + (cateto2**2))
print('A hipotenuda entre {} e {} é de {:.2f}'.format(cateto1, cateto2, hipotenusa))