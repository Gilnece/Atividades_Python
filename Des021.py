# faça um programa que leia um número de 0 a 9999 e mostre na tela
# cada um dos digitos separados
# Ex: Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

num = int(input('Digite um numero entre 0 e 9999: '))
#n = num.zfill(4) # preenche com zeros a esquerda se caso o numero tenha menos de 4 digitos

'''un = n[3]  #|
dez = n[2] #|
#             |-> O NUMERO INDICA O INDICE QUE DEVE SER EXIBIDO
cen = n[1] #|
mi = n[0]  #|'''

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

'''print(f'Unidade: {un}')
print(f'Dezena: {dez}')
print(f'Centena: {cen}')
print(f'Milhar: {mi}')'''

print('Unidade:{}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
