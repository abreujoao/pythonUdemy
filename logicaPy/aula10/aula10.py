"""
if e else
"""
"""
idade= 18

idade=int(input('idade:'))

if idade >= 18:
    print('ele é de maior')
elif idade <= 18:
    print('ele é de menor')

"""
'''treino de logica'''
"""'

name='joao'
ano: int=2002

ano=int(input('ano de nascimento de '))

if ano == 2002:
    print('ano correto')
elif ano != 2002:
    print('ano incorreto')

##########################################
n1= float(input('digite a primeira nota do aluno'))
n2=float(input('digite a segunda nota do aluno'))
n3= float(input('digite a terceira nota aluno'))
m= (n1+n2+n3)/3

if m >= 7.0:
    print('você passou de ano')
else:
    print('infelizmente voce não passou de ano')


#########################################

name=str(input('Qual o seu nome?'))

if name == 'joao':
    print('nome correto')
else:
    print('nome incorreto')
    
######################################### """
print('Seja bem vindo ao nosso cadrasto, é um prazer a sua presença, vamos começar?')
print("")


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