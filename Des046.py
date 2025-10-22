'''faça um programa que calcule a soma entre todo os números impares que são
múltiplos de três e que se encontram no intervalo de 1 até 500'''
for c in range(0, 500):
    if c % 2 == 1: # numeros impares
        if c % 3 == 0: # numeros multiplos de 3
            print(c)