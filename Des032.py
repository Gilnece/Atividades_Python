'''Escreva um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento.
Para salários superiores a 1250,00R$, calcule um aumento de 10%
Para salarios inferiores ou iguais, o aumento é de 15%'''

salario = float(input('Qual seu salario: '))
if salario > 1250:
    ajuste = salario * 10/100
    nsalario = salario + ajuste
    print('Seu aumento foi de 10%, ajuste ficou em {} e o novo salario ficou: {}'.format(ajuste, nsalario))
if salario <= 1250:
    ajuste = salario * 15/100
    nsalario = salario + ajuste
    print('Seu aumento foi de 15%, ajuste ficou em {} e o novo salario ficou: {}'.format(ajuste, nsalario))
