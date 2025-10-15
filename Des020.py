#crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas as letras maiusculas
# o nome com todas minúsculas
# quantas letras ao todo(sem considerar espaços
# quantas letras tem o primeiro nome

nome = input('Digite seu nome: ')

print('Nome com todas as letras Maiúsculas: ', nome.upper())
print('Nome com todas as letras Menusculas: ', nome.lower())
print('seu nome tem',len(nome.replace(" ", "")),'letras')
pnome = nome.split()[0]
print('O nome', pnome,'tem',len(pnome), 'letras')