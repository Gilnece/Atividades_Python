'''crie um programa que mostre na tela todos os números pares que estão
no intervalo entre 1 e 50'''

print('\nEssa é a lista de todos os numeros pares entre 1 e 50:')
for c in range(0, 50):
    par = c % 2
    if par == 0:
        print(c)
