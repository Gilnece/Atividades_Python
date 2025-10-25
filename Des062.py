'''Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos'''

a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))

n_termos = 10  # <--- numero determinado pela questão, a quantidade de termos a aparecer
termo_atual = a1  # <--- Variável para guardar o termo que irá iniciar
totexib = 0

while True:
    cont = 1
    while cont <= n_termos:  # vai repetir enquanto o contador for menor ou igual a 10,ou seja, o programa exibirá 10 termos
        print('{} → '.format(termo_atual), end='')
        termo_atual += r  # Atualiza o termo: soma a razão ao termo atual para obter o próximo.
        cont += 1  # Aumenta o contador em 1, indicando que um termo foi exibido.
        totexib += 1

    print('FIM')
    print('~' * 30)

    mais = int(input('Termos exibidos até agora: {}.\n Quantos termos você quer exibir a mais? '.format(totexib)))
    if mais == 0:
        break
    else:
        n_termos = mais # se deixar com += ele irá aparecer uma linha gigante com muitos termos em seguida
print('FIM')
print('Total de termos exibidos: {}'.format(totexib))