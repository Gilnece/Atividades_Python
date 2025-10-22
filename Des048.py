'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for impar desconsidere-o'''

soma = 0 #iniciar a soma sem valor nenhum para trabalhar ele posteriormente
cont = 0
for c in range(1, 6+1):
    n = int(input('Digite o {}º numero inteiro: '.format(c)))
    if n % 2 == 0: # irá destacar apenas o numeros pares
        soma += n # soma os valores listados acima
        cont += 1
print('{} numeros pares foram encontrados e a soma dos numero pares é: {}'.format(cont, soma))
if n % 2 == 1:
    print('Nenhum numero PAR encontrado!')
