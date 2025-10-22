'''crie um programa que mostre na tela todos os números pares que estão
no intervalo entre 1 e 50'''

print('\nEssa é a lista de todos os numeros pares entre 1 e 50:')
for c in range(1, 50+1): # para 2, 51, 2 é feito metade das interações
    par = c % 2
    if par == 0: # para o metodo anterior falado não precisaria desse if
        print(c, end=' ') # end faz não pular a linhas
print('\nEsses são todos os numeros pares encontrados nessa condição')
