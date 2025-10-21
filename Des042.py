'''elabore um programa que calcule o valor a ser pago por um produto
considerando o seu preço normal e condição de pagamento
a vista dinheiro ou cheque:10% de desconto
a vista no cartão: 5% de desconto
em até 2x no cartão: preço normal
3x ou mais no cartão: 20% de juros'''

from time import sleep
computador = 7000
print('o computador vai custar R${:.2f}'.format(computador))


while True:
    print('\n===MENU PRINCIPAL===')
    print('1 - A vista')
    print('2 - Cartão 1x')
    print('3 - Cartão 2x')
    print('4 - Cartão 3x+')
    print('5 - Sair\n')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
         vista = computador - (computador * 0.10)
         print('10% de desconto aplicado!')
         print('\033[1;31mPROCESSANDO PAGAMENTO...\033[0m')
         sleep(2)
         print('A vista no pix ou dinheiro o valor ficou em R${:.2f}'.format(vista))
         break
    elif opcao == '2':
        cartao1x = computador - (computador * 0.05)
        print('5% de desconto aplicado!')
        print('\033[1;31mPROCESSANDO PAGAMENTO...\033[0m')
        sleep(2)
        print('A vista no cartão ficou em R${:.2f}'.format(cartao1x))
        break
    elif opcao == '3':
        cartao2x = computador
        print('Compra sem desconto!')
        print('\033[1;31mPROCESSANDO PAGAMENTO...\033[0m')
        sleep(2)
        print('2x no catão ficou em R${:.2f}'.format(cartao2x))
        break
    elif opcao == '4':
        cartao3x = computador + (computador * 0.20)
        print('20% de juros aplicado!')
        print('\033[1;31mPROCESSANDO PAGAMENTO...\033[0m')
        sleep(2)
        print('3x ou mais no cartão ficou em R${:.2f}'.format(cartao3x))
        break
    elif opcao == '4':
        break
    else:
        print('Opção invalida! Tente novamente')

