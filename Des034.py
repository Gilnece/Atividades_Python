'''Escreva um programa que aprove um emprestimo bancario
para a compra de uma casa. O programa vai perguntar o VALOR DA CASA, o SALARIO
do comprador e em QUANTOS ANOS ele vai pagar.
Calcule o calor da prestação mensal, sabendo que ela não pode exceder a 30%
do salario ou então o emprésto será negado'''


print('Bem vindo a COMPRECASA, vamos consultar seu credito?')

vcasa = float(input('Digite o valor da casa: '))
salario = float(input('Quanto recebe por mes: '))
qt_anos = int(input('Em quantos anos pretende pagar: '))

entrada = input('terá entrada?')
mensalidade = qt_anos * 12

if entrada == 'sim' or tera == 'sim':
    vlentrada = float(input('Digite o valor de entrada: '))
    prestacao = (vcasa - vlentrada) / mensalidade
else:
    prestacao = vcasa / mensalidade

analise = salario * 0.3

if prestacao > analise:
    print('Infelizmente seu credito não foi aprovador')
    print('o valor da prestação ficaria em R${:.2f}, 30% do seu salario é: R${:.2f}'.format(prestacao, analise))
    print('\033[1;31mEmpréstimo Negado\033[0m')
elif prestacao < analise:
    print('\033[1;32mCredito aprovado com sucesso\033[0m')
    print('o valor da prestação ficaria em R${:.2f}, 30% do seu salario é: R${:.2f}'.format(prestacao, analise))

