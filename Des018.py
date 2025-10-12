# o mesmo professor do desafio anterior quer sortear a ordem de apresentação de
#trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a
#ordem sorteada

import Desafios.Des017
import random

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

nomes = [aluno1, aluno2, aluno3, aluno4]
ordem = random.shuffle(nomes) #A função shuffle irá embaralhar a ordem antes estabelecida
#mesmo que seja em seguida mandado exibir os nomes em tela, ele não irá

print('a ordem das apresentações será: {} '.format(nomes))