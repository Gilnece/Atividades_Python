'''faça um progrma que leia o sexo de uma pessoa, mas só aceite os valores M ou F
caso esteja errado peça a digitação novamente até ter um valor correto'''

sexo = str(input('Digite o sexo [M/F]: ')).upper() # escrever o sexo, será transformado em maiusculo
while sexo != 'M' and sexo != 'F': # se a resposta for diferente de M ou F, vai ficar pedindo para informar a opção correta
    sexo = str(input('Opção invalida, digite o sexo [M/F]: ')).upper()
print('Sexo {} registrado com sucesso!'.format(sexo))
