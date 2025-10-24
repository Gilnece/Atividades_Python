'''Crie um programa que leia uma frase qualquer e diga se ela é um
palindromo, desconsiderando os espaços'''
#palindromo são palavras ou frases que podem ser lidas iguais de trás para frente
#apos a sopa
#a sacada da casa
#a torre da derrota
#o lobo ama o bolo
#anotaram a data da maratona

texto = str(input('Digite uma frase qualquer: '))
frase = texto # armazenar o testo para exibir no final
texto = texto.replace(' ', '').lower() # tratando o texto para tirar os espaços e deixar menusculo
if texto == texto[::-1]: # comparando frase inicial com o oposto dela
    print('A frase {} ao contrario é {}'.format(texto.upper(), texto[::-1].upper())) # adicionado metodo para mostrar a frase e o seu contrario
    print('Se enquadra como um palindromo')
else:
    print('A frase {} não forma um palindromo'.format(frase.upper()))
