num  = int(input('Informe quantos numeros irá exibir: '))
a = 0 # a sequencia de Fibonacci começa sempre sem zero
b = 1 # o numero que vem em seguida é o proximo depois do primeiro numero da sequencia, porém a questão quer que seja digitado um numero inteiro e venha a calcular a partir dele

cont = 2
print(a, end=' → ')
print(b, end=' → ')
while cont < num:
    c = a + b # irá somar o primeiro e o segundo termo
    print(c, end=' → ')
    a = b # faz o primeiro termo receber o termo anterior
    b = c # faz o segundo termo receber o somatorio do primeiro e o segundo termo anteriores
    cont += 1
'''    if cont > 30:
        print('\n')''' # metodo pensado em numeros muito grandes para linha impressa não seja gigantesca
print('FIM')