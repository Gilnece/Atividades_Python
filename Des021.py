# faça um programa que leia um número de 0 a 9999 e mostre na tela
# cada um dos digitos separados
# Ex: Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

num = input('Digite um numero entre 0 e 9999: ')[:4]#<- limita o numero a 4 caracteres
num = num.zfill(4) # preenche com zeros a esquerda se caso o numero tenha menos de 4 digitos

un = num[3]  #|
dez = num[2] #|
#             |-> O NUMERO INDICA O INDICE QUE DEVE SER EXIBIDO
cen = num[1] #|
mi = num[0]  #|

print(f'Unidade: {un}')
print(f'Dezena: {dez}')
print(f'Centena: {cen}')
print(f'Milhar: {mi}')
