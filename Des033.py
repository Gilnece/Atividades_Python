'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo.'''

'''Exemplo:
r1: 3cm
r2: 5cm
r3: 6cm
essas medidas formam um triangulo'''

'''As condições que devem ser satisfeitas são:     
A soma dos lados a e b deve ser maior que o lado c: a+b>c. 
A soma dos lados a e c deve ser maior que o lado b: a+c>b. 
A soma dos lados b e c deve ser maior que o lado a: b+c>a.'''
print('- Medidas em cm -')
a = float(input('Qual a medida da primeira lado: '))
b = float(input('Qual a medida da segunda lado: '))
c = float(input('Qual a medida da terceira lado: '))


if (a + b > c) and (a + c > b) and (b + c > a):
    print('Um triangulo pode ser formado')
else:
    print('Um triangulo nao pode ser formado')