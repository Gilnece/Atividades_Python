'''refaça o sesafio 033 dos triangulos. acrescentando o recurso de mostrar que tipo de triangulo será formad:
equilatero: todos os lados iguais
isoceles: dois lados iguais
escaleno: todos os lados diferentes

Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo.'''

l1 = float(input('Digite o lado 1: '))
l2 = float(input('Digite o lado 2: '))
l3 = float(input('Digite o lado 3: '))

if (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2):
    if l1 == l2 == l3: # equilatero
        print('um triangulo equilatero pode ser formado')
    elif l1 == l2 or l1 == l3 or l2 == l3: #isoceles
        print('um triangulo isoceles pode ser formado')
    else: #escaleno
        print('um triangulo escaleno pode ser formado')
else:
    print('Não é possivel formar um triangulo')