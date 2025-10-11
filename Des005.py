#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2

peso1 = (nota1 * 0.4)
peso2 = (nota2 * 0.6)
mediapeso = (peso1 + peso2) / 2

print('Média do aluno é: {}'.format(media))
print('Média do aluno com 4 para primeira nota e 6 para segunda nota: {}'.format(mediapeso))
