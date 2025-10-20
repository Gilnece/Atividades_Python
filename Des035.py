'''Escreca um programa que leia um numero inteiro
qualquer e peça para o usuario escolher qual será a base de conversão
1 para binario
2 para octal
3 para hexadecimal'''

num = int(input('Digite um numero inteiro: '))

while True:
    print('\n===MENU PRINCIPAL===')
    print('1 - Binario')
    print('2 - Octal')
    print('3 - Hexadecimal')
    print('4 - Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        bin = bin(num)[2:] #[2:] serve para remover o prefixo 0b
        print('O numero {} convertido para Binario apresenta o seguinte valor: {}'.format(num, bin))
    elif opcao == '2':
        oct = oct(num)
        print('O numero {} convertido para Binario apresenta o seguinte valor: {}'.format(num, oct))
    elif opcao == '3':
        hex = hex(num)
        print('O numero {} convertido para Binario apresenta o seguinte valor: {}'.format(num, hex))
        break
    elif opcao == '4':
        break
    else:
        print('Opção invalida! Tente novamente')