#Escreva um programa que pergunte a quantidade de Km percorridos por um carro
#alugado e a quantidade de dias pelos quais ele foi alugado.
#Caulcule o preço a pagar sabendo que o carro custa R$60 por dia e 0,15 por Km rodado

km = float(input('Quantos Km foram rodados: '))
dia = int(input('Quantos dias de locação: '))

kmlocacao = km * 0.15
dialocacao = dia * 60

locacao = kmlocacao + dialocacao

print('A locação durou {} dias e foram rodados {:.3f} Km, gerando uma fatura de R${:.2f}'.format(dia, km, locacao))

