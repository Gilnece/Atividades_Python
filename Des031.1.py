'''faça um programa que leia três numeros e mostre qual é o maior e qual é o menor'''

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite mais um numero: '))

lista = [n1, n2, n3]

if max(lista) > min(lista):
    print('O maior numero é: {}'.format(max(lista)))
    print('O menor numero é: {}'.format(min(lista)))
