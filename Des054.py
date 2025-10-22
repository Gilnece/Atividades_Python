'''desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
A média de idade do grupo
qual é o nome do homem mais velho
quantas mulheres têm menos de 20 anos'''

# Inicializando variáveis
soma_idade = 0
homem_mais_velho = ''
idade_homem_mais_velho = 0
mulheres_menores_20 = 0

# Loop para cadastrar 4 pessoas
for c in range(1, 5):
    print(f'----- {c}ª Pessoa -----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').strip().upper()  # padroniza entrada

    # Soma das idades para calcular a média
    soma_idade += idade

    # Verifica se é homem e se é o mais velho
    if sexo == 'M':
        if idade > idade_homem_mais_velho:
            idade_homem_mais_velho = idade
            homem_mais_velho = nome

    # Conta mulheres com menos de 20 anos
    if sexo == 'F' and idade < 20:
        mulheres_menores_20 += 1

# Cálculo da média de idade
media_idade = soma_idade / 4

# Resultado final
print('----- RESULTADOS -----')
print(f'A média de idade do grupo é {media_idade:.1f} anos.')
print(f'O homem mais velho é: {homem_mais_velho}')
print(f'Número de mulheres com menos de 20 anos: {mulheres_menores_20}')
