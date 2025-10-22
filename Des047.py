'''Refaça o desafio 007, mostrando a tabuada de um número que o usuário escolher, só que
agora utilizando um laço for'''

num = int(input('Digite um numero inteiro: '))
for c in range(1, 10+1): # contagem irá começar em 1 e irá ignorar a ultima casa, terminando em 10
    print('{} x {} = {}'.format(num, c, c*num))
