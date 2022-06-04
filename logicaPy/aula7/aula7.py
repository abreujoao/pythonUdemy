"""
 Introdução à formatação de Strings
"""

nome="João Paulo"
idade = 19
altura= 1.70
eMaior= idade>18
peso=80
imc=peso/(altura **2)


print(nome,'tem', idade, 'de idade e seu imc é', imc)

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f} ')

