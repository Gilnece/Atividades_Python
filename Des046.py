'''faça um programa que calcule a soma entre todo os números impares que são
múltiplos de três e que se encontram no intervalo de 1 até 500'''
soma = 0
cont = 0
for c in range(0, 500+1):
    if c % 2 == 1: # numeros impares
        if c % 3 == 0: # numeros multiplos de 3
            soma = soma + c # realizar a soma de todos os numeros informados
            cont = cont + 1 # realiza a contagem de quantas interações foram feitas
print('A soma entre todos os numeros solicitados é {}'.format(soma))
print('{} numeros foram encontrados'.format(cont))

