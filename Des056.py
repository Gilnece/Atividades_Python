'''crie um script que faça um login simples
deve ser feito uma validação para saber se nome e senha estão corretos
se estiver correto, irá exibir uma mensagem de bom dia
nome correto + senha errada = senha incorreta
nome errado + senha incorreta = usuario não encontrado'''

print('Vamos ao cadastro')
name = input('Digite seu nome: ')
password = input('Digite sua senha: ')

print('\nLogin')
usuario = input('Usuario: ')
senha = input('Senha: ')

if usuario == name and senha == password:
    print('ola {} seja bem vindo'.format(name))
elif usuario != name and senha == password:
    print('Usuario não encontrado')
elif usuario == name and senha != password:
    print('Senha incorreta!')
else:
    print("Usuário não encontrado!")
