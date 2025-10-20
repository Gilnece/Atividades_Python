'''escreca um programa que leia DOIS NUMEROS inteiros e compare-os.
mostrando na tela uma mensagem:
- o primeiro valor é maior
o segundo valor é maior
não existe valor maior, os dois são iguais'''

n1 = int(input('Digite um valor inteiro: '))
n2 = int(input('Digite outro valor inteiro: '))
if n1 > n2:
    print('o primeiro valoré maior que o segundo!')
elif n1 < n2:
    print('o segundo valor é maior que o primeiro!')
elif n1 == n2:
    print('Os dois numeros tem o mesmo valor!')
