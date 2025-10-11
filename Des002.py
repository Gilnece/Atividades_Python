#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
#possiveis sobre ela

dado = input('Digite algo: ')

print('o tipo primitivo dessa informação é:', type(dado))
print('é um numero?', dado.isnumeric())
print('é alfabetico?', dado.isalpha())
print('é alfanumerico?', dado.isalnum())
print('está tudo maiusculo?', dado.isspace())
print('está todo menusculo?', dado.islower())
print('são somente espaços?', dado.isspace())
