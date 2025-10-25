'''refaça o desafio 049, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while'''

a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
n_termos = 10 # <--- numero determinado pela questão, a quantidade de termos a aparecer
cont = 1
termo_atual = a1 # <--- Variável para guardar o termo que irá iniciar

while cont <= n_termos: #vai repetir enquanto o contador for menor ou igual a 10,ou seja, o programa exibirá 10 termos
    print('{} → '.format(termo_atual), end='')
    termo_atual += r # Atualiza o termo: soma a razão ao termo atual para obter o próximo.
    cont += 1 # Aumenta o contador em 1, indicando que um termo foi exibido.
print('Fim')