'''desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
A média de idade do grupo
qual é o nome do homem mais velho
quantas mulheres têm menos de 20 anos'''

p = int(input('Quantas pessoas iram ser analisadas? '))

if p < 0:
    print('Nenhuma pessoa para analisar!')
else:
    # Inicializando variáveis
    soma_idade = 0
    homem_mais_velho = ''
    idade_homem_mais_velho = 0
    mulheres_menores_20 = 0

    # Loop para analisar a quantidade de pessoas informada anteriormente
    for c in range(1, p+1):
        print('----- {}ª Pessoa -----'.format(c))
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
    media_idade = soma_idade / p

    # Resultado final
    print('----- RESULTADOS -----')
    print('A média de idade do grupo é {:.2f} anos.'.format(media_idade))
    print('O homem mais velho é: {}'.format(homem_mais_velho))
    print('Número de mulheres com menos de 20 anos: {}'.format(mulheres_menores_20))

