#Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salário, com 15% de aumento

salario = float(input('Digite o seu salario:R$ '))

aumento = salario * 0.15
novo_salario = salario + aumento

print('Seu novo salario será de {}'.format(novo_salario))
