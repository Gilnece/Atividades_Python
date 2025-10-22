'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for impar desconsidere-o'''

soma = 0 #iniciar a soma sem valor nenhum para trabalhar ele posteriormente
for c in range(0, 6):
    n = int(input('Digite um numero inteiro: '))
    if n % 2 == 0: # irá destacar apenas o numeros pares
        soma += n # soma os valores listados acima
print ('A soma dos numero pares é: {}'.format(soma))
if n % 2 == 1:
    print('Nenhum numero PAR encontrado!')