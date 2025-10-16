#crie um programa que leia o nome de uma cidade e diga se ela começa
#ou não com o nome "santo".

cid = input('digite o nome de uma cidade: ')
#verifica se o nome da cidade começa com 'Santo'
if cid.strip().lower().startswith('santo'):
    print('a cidade contem a "Santo".')
else:
    print('a cidade não contem a "Santo".')

#STRIP: remove espaços entras no inicio e no final da string, garantindo que a verificação não falhe
#LOWER: converte a string para minusculas, tornando a comparação insensível a maiusculas, tudo será tratado igual

#STARTSWITH:verifica se a string começa com a palavra informada
'''sugestão do professor
cidade = str(input('digite o nome de uma cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')'''
