'''desenvolva uma logica que leia o peso e altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
abaixo de 18.5: abaixo do peso
entre 18.5 e 25: peso ideal
25 a 30: sobrepeso
30 a 40:: obesidade
acima de 40 obesidade morbida'''

# IMC = (peso /(altura x altura)) / 2
peso = float(input('Digite o peso em Kg: '))
altura = float(input('Digite sua altura em Metros: '))

imc = (peso / (altura * altura))
if imc < 18.5:
    print('Seu IMC é: {:.2f}. Você está abaixo do peso'.format(imc))
elif  18.5 < imc < 25:
    print('Seu IMC é: {:.2f}. Você está no peso ideal'.format(imc))
elif 25 < imc < 30:
    print('Seu IMC é: {:.2f}. Você está com sobrepeso'.format(imc))
elif 30 < imc < 40:
    print('Seu IMC é: {:.2f}. Você está com Obesidade'.format(imc))
elif imc >= 40:
    print('Seu IMC é: {:.2f}. Você está com Obesidade Morbita'.format(imc))