'''Refaça o desafio 007, mostrando a tabuada de um número que o usuário escolher, só que
agora utilizando um laço for'''

num = int(input('Digite um numero inteiro: '))
for c in range(1, 11): # contagem irá começar em 1 e irá ignorar a ultima casa, terminando em 10
    calculo = num * c # calcular o valor digitado multiplicado pelo range do for
    print('{} x {} = {}'.format(num, c, calculo))
