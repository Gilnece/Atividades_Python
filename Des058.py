'''melhor o jogo do desafio 026 onde o computador vai "pensar" em um numero entre 0 e 10.
So que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer'''

from random import randint # biblioteca para escolher numeros aleatorios
computador = randint(0, 10) # faixa entre 0 e 10
cont = 1 # inicializando um contador em 1
while True: # enquanto for verdadeira a condição a seguir
    jogador = int(input('Digite um numero entre 0 e 10: ')) # informar o numero da tentativa
    if jogador == computador: # quando o resultado for igual ao do computador finaliza
        break
    if jogador != computador: # enquanto for diferente vai contar mais um
        if computador < jogador:
            print('Menos... tente novamente')
        elif computador > jogador:
            print('Mais... tente novamente')
        cont += 1 # antes iniciado em 1, adiciona mais 1
        continue
print('Voce venceu com {} palpites.'.format(cont)) # no final vai escrever quantas tentativas foram para acertar
