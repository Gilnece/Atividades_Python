'''crie um programa que leia dois valores e mostre um menu na tela:
1 - somar
2 - multiplicar
3 - maior
4 - novos números
5 - sair do programa'''
from time import sleep

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
while True:
    print('1 - somar')
    print('2 - multiplicar')
    print('3 - maior')
    print('4 - novos números')
    print('5 - sair')

    opcao = int(input('Escolha: '))
    if opcao == 1:
        soma = n1 + n2
        print('{} + {} = {}'.format(n1, n2, soma))
    if opcao == 2:
        multiplicar = n1 * n2
        print('{} x {} = {}'.format(n1, n2, multiplicar))
    if opcao == 3:
        if n1 > n2:
            maior = n1
            print('{} maior que {}'.format(maior, n2))
        else:
            maior = n2
            print('{} maior que {}'.format(maior, n1))
    if opcao == 4:
        print('Digite numeros novos')
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor: '))
    if opcao == 5:
        print('Saindo do programa...')
        sleep(1)
        break