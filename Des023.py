#crie um programa que leia o nome de uma pessoa e diga se ela tem "silva"
# no nome.

print('Vamos descobrir se você é um Silva!')
nome = input('Digite seu nome: ')

if 'silva' in nome.lower():
    print('Achamos mais um Silva')
else:
    print('Você não é um Silva!')

#lower faz com que toda a frase seja convertida em menusculo, fazendo com que a verificação seja mais precisa

'''metodo alternativo
nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))'''
