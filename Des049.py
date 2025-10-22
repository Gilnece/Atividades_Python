'''desenvolva um programa que leia o primeiro termo e a razão de um PA.
No final, mostre os 10 primeiros termos dessa progressão'''
#PA - progressão aritmetica

a1 = int(input('Digite o primeiro digito do termo: '))
r = int(input('Digite a Razão da PA: '))
an = int(input('Informe o ultimo digito do termo: '))

cont = 0  # iniciando contador
print('-=-'*10)
print('10 PRIMEIROS TERMOS DE UMA PA')
print('-=-'*10)
for pa in range(a1, an + 1, r):
    print('{}'.format(pa), end='➜ ')
    cont += 1
    if cont == 10:  # para quando chegar a 10 termos, pare de exibir
        break
print('FIM')
