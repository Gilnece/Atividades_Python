'''elabore um programa que calcule o valor a ser pago por um produto
considerando o seu preço normal e condição de pagamento
a vista dinheiro ou cheque:10% de desconto
a vista no cartão: 5% de desconto
em até 2x no cartão: preço normal
3x ou mais no cartão: 20% de juros'''

from time import sleep
preco = float(input('Digite o preço das compras: '))

while True:
    print('\n===FORMA DE PAGAMENTO===')
    print('1 - A vista')
    print('2 - A vista no cartão')
    print('3 - 2x no cartão')
    print('4 - 3x ou mais no cartão')
    print('5 - Sair\n')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
         vlcompra = preco - (preco * (10 / 100))
         print('\033[1;31mPROCESSANDO PAGAMENTO...\033[0m')
         sleep(2)
         print('10% de desconto aplicado!')
         print('compra de R${:.2f} a vista ficou em R${:.2f} COM DESCONTO'.format(preco, vlcompra))
         break
    elif opcao == '2':
        vlcompra = preco - (preco * 0.05)
        print('\033[1;31mPROCESSANDO PAGAMENTO...\033[0m')
        sleep(2)
        print('5% de desconto aplicado!')
        print('Compra de R${:.2f} a vista no cartão ficou em R${:.2f} COM DESCONTO'.format(preco, vlcompra))
        break
    elif opcao == '3':
        vlcompra = preco
        parcela = vlcompra / 2
        print('\033[1;31mPROCESSANDO PAGAMENTO...\033[0m')
        sleep(2)
        print('Sua compra de R${:.2f} foi parcelada em 2x no cartão, ficou em R${:.2f} SEM JUROS!\nValor das parcelas: R${:.2f}'.format(preco,vlcompra, parcela))
        break
    elif opcao == '4':
        vlcompra = preco + (preco * 0.20)
        qtparcelas = int(input('Quantas parcelas? '))
        parcela = vlcompra / qtparcelas
        print('\033[1;31mPROCESSANDO PAGAMENTO...\033[0m')
        sleep(2)
        print('sua compra de R${:.2f} foi parcelado em {}x no cartão, ficou em R${:.2f} COM JUROS\nValor das parcelas: R${:.2f}'.format(preco, qtparcelas, vlcompra, parcela))
        break
    elif opcao == '4':
        break
    else:
        print('Opção invalida! Tente novamente')
