#escreva um programa que converta uma temperatura difitando em graus celsius e converta para graus fahrenheit

temp = float(input('Digite a temperatura: '))

fah = temp *(9/5) + 32

print('{:.2f}ºC equivalem a {:.2f}ºF'.format(temp, fah))
