'''desenvolva um programa que leia o primeiro termo e a razão de um PA.
No final, mostre os 10 primeiros termos dessa progressão'''
#PA - progressão aritmetica

a1 = int(input('Digite o primeiro digito do termo: '))
r = int(input('Digite a Razão da PA: '))
an = int(input('Informe o ultimo digito do termo: '))

contador = 0  # vai contar quantos termos foram exibidos

for termo in range(a1, an + 1, r):
    print(termo)
    contador += 1
    if contador == 10:  # para quando chegar a 10 termos, pare de exibir
        break
