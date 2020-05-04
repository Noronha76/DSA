
# atribuição condicional
idade = 15
texto = "maior de idade" if idade >=18 else "menor de idade"

# comparação dupla
x = 8
if 0 < x < 10:
    print('é um número positivo de um dígito')
# print('é um número positivo de um dígito') if 0 < x < 10 ERRO!!!

# 
a = 2
b = 3
a,b = b,a

#Recursividade 
def countdown(n):
    if n <= 0:
        print('blastoff')
    else:
        print(n)
        countdown(n-1)