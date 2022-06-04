name = str(input('Qual o seu nome?'))
idade = int(input('Qual a sua idade?'))
anoNascimento = int(input('Qual o seu ano de nascimento'))
peso = float(input('Qual o seu peso'))

if idade >= 18:
    print('Você é maior de idade e está apto a participar do nosso programa!')
else:
    print('Você não tem idade para partipar.')


if anoNascimento <= 2004:
    print('Você é de maior confirmado.')
else:
    print("Não tente nos enganar.")

if peso >= 75:
    print('Você está com peso alto')
else:
    print('Seu peso está de acordo')