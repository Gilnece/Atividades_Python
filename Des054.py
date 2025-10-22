'''desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
A média de idade do grupo
qual é o nome do homem mais velho
quantas mulheres têm menos de 20 anos'''

# Inicializando variáveis
s_idade = 0 # soma das idades
hmv = '' # homem mais velho
ihmv = 0 # idade do homem mais velho
mu_men_20 = 0 # mulheres menores que 20 anos

for c in range(1, 5): # Loop para cadastrar 4 pessoas
    print('----- {}ª Pessoa -----'.format(c))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').strip().upper()  # padroniza entrada
    # Soma das idades para calcular a média
    s_idade += idade

    if sexo == 'M': # Verifica se é homem e se é o mais velho
        if idade > ihmv:
            ihmv = idade
            hmv = nome

    if sexo == 'F' and idade < 20: # Conta mulheres com menos de 20 anos
        mu_men_20 += 1

media_idade = s_idade / 4 # Cálculo da média de idade

# Resultado final
print('----- RESULTADOS -----')
print('A média de idade do grupo é {:.1f} anos'.format(media_idade))
print('O homem mais velho é: {}'.format(hmv.capitalize()))
print('Número de mulheres com menos de 20 anos: {}'.format(mu_men_20))
