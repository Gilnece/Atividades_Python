#faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o últiumo nome separadamente
#ex: Ana Maria de Souza
#primeiro = Ana
# Ultimo = Souza

nome = str(input('Digite seu nome completo: ')).strip()
pnome = nome.split()[0] # realiza a contagem da primeira palavra
unome = nome.split()[-1] #realizar a contagem da ultima palavra
'''extra
snome = nome.split()[1]
tnome = snome.split()[2]
qnome = snome.split()[3]'''

print('O primeiro nome é: {}'.format(pnome))
print('O ultimo nome é: {}'.format(unome))
'''print(snome)
print(tnome)
print(qnome)'''
