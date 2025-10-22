'''crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores'''

from datetime import date
pessoas = int(input('Quantos seram analisados? ')) # criado metodo posteriormente para definir quantas pessoas teram sua idade analisada
menor = 0 # iniciar contagem em zero
maior = 0 # iniciar contagem em zero
for i in range(1, pessoas+1): # criar um range que inicia em 1 e vai até 6, que também pode ser escrito com 6+1
    idade = int(input('Digite seu ano de nascimento: '))
    if date.today().year - idade < 18:
        menor += 1 # será feita uma contagem na lista de pessoas menores de idade
    else:
        maior += 1 # será feita uma contagem na lista de pessoas maiores de idade
print('{} são menores de idade'.format(menor))
print('{} são maiores de idade'.format(maior))