
nome=(input('Bom dia, muito obrogado por entrar emnosso programa, como você se chama?'))

print('')

numero= input(f'Certo {nome}, agora peço para que digite um numero, e na volta direi se ele é par ou impar')

if numero.isdigit():
    numero=int(numero)

    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")
else:
    print(' isso não é um número inteiro')

#######################################################

#data e hora

horario=input('Digite um horario (0-23): ')


if horario.isdigit():
    horario=int(horario)

    if horario <0 or horario > 23:
        print("o horario deve estar entre o e 23")
    else:
        if horario <= 11:
            print('bom dia')
        elif horario <=17:
            print('BOA TARDE')
        else:
            print("boa noite")
else:
    print("Por favor, digite um horario entre 0 e 23")


###################


name= input('digite o seu nome:')
tamanho=len(name)

if tamanho <=4:
    print("o seu nome é curto")
elif tamanho <=6:
    print('seu nome é normal')
else:
    print('seu nome é muito grande')





