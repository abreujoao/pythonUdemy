"""
Documentação e funções built-in úteis
"""


n1= input('digite o primeiro numero')
n2= input('digite o segundo numero')

try: #tenta
    n1=float(n1)
    n2=float(n2)

    print(n1+n2)

except:
    print('ERROR')
