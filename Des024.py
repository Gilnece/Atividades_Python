#faça um programa que leia uma frase pelo teclado e mostre:
#quantas vezes aparece a letra "A".
#em que posição ela aparece a primeira vez.
#em que posição ela aparece a última vez.

frase = input('Digite uma frase: ').strip()

print('A letra "A" se repete ',frase.upper().count('A'),'vezes!')
print('A letra "A" aparece pela primeira vez na posição:',frase.upper().find('A')+1)
print('A letra "A" aparece pela ultima vez na posição:',frase.upper().rfind('A')+1)

#upper vai fazer todas as letras da frase ficarem maiusculas
#count irá fazer a contagem do conteudo desejado
#find informa qual posição aquela informação é encontrada, +1 pois ele para a contagem 1 posição antes, então deve informar o +1 para pular a casa.
#rfind inverte o sentido da contagem, também precisa de um +1 para inforamar a casa que a informação se encontra
#strip foi adicionado para remover os espaços indesejados
