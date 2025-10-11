#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input('Qual o preço do produto: R$ '))

desconto = preco * 0.05
valor = preco - desconto

print('{}R$ com 5% de desconto fica a {}R$ com desconto'.format(preco, valor))

