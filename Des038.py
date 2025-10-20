'''crie um programa que leia duas notas de um aluno e calcule
sua média, mostrando uma mensagem no final, de acordo com a média atingida:
média abaixo de 5: reprovado
média entre 5 e 6.9: recuperação
media 7 ou superior: aprovado'''

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))


while True:
    print('\n===MENU PRINCIPAL===')
    print('1 - Média sem pesos')
    print('2 - média com pesos')
    print('3 - Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        media = (nota1 + nota2) / 2

        reprovado = media < 5
        recuperacao = 5 < media < 7.9
        aprovado = media >= 7.9

        if reprovado:
            print('\033[1;31msua média foi {} vocês está Reprovado!\033[0m'.format(media))
        elif recuperacao:
            print('\033[1;33msua media foi {}, estude mais para passar!\033[0m'.format(media))
        elif aprovado:
            print('\033[1;32mParabéns com média {}, Você está aprovado!\033[0m'.format(media))
        break
    elif opcao == '2':
        p1 = float(input('Digite o primeiro peso: '))
        p2 = float(input('Digite o segundo peso: '))

        media = ((nota1 * p1) + (nota2 * p2)) / (p1 + p2)

        reprovado = media < 5
        recuperacao = 5 < media < 7.9
        aprovado = media >= 7.9

        if reprovado:
            print('\033[1;31msua média foi {} vocês está Reprovado!\033[0m'.format(media))
        elif recuperacao:
            print('\033[1;33msua media foi {}, estude mais para passar!\033[0m'.format(media))
        elif aprovado:
            print('\033[1;32mParabéns com média {}, Você está aprovado!\033[0m'.format(media))
        break
    elif opcao == '3':
        break
    else:
        print('Opção invalida! Tente novamente')