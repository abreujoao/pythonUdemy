 #while True +1:    #loop infinito
   # nome=print(input('qual o seu nome'))
    #print(f'olá {nome}')

'''
x=0

while x < 10:
    if x == 3:
        x =x+1
        break

    print(x)
    x = x + 1

print('acabou')
'''

'''x = 0

while x < 10:
    y = 0
    print(f'x vale {x} e y vale {y}')
    y += 1

    x += 1

print("acabou")'''

'''while True:
    print()
    num1 = input("digite um numero")
    num2 = input("digite um numero")
    operador=input('digite um operador')

    if not num1.isnumeric() or not num2.isnumeric():
        print('voce precisa digitar um numero')
        continue

    num1=int(num1)
    num2=int(num2)

    if operador == '+':
        print(num1+num2)
    if operador == '-':
        print(num1-num2)
    if operador == '*':
        print(num1*num2)
    if operador == '/':
        print(num1/num2)'''

contador = 0

while contador <= 100 :
    print(contador)
    contador+=1

