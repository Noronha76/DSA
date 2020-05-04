#exercício
# 02 versão DSA:
palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()
resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
for i in resultado:
    print(i)
    #print(i)
print('-------------------------')


# 02 CFTN:
palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()
[print(w.upper(), w.lower(), len(w)) for w in palavras]
print('-------------------------')


# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
# Caso não saiba o que é matriz transposta, visite este link: https://pt.wikipedia.org/wiki/Matriz_transposta
# Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de sistemas de IA.
matrix = [[1, 2],[3,4],[5,6],[7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print(transpose)
print('-------------------------')

# 04 DSA:
lista = [0, 1, 2, 3, 4]

def square(x):
        return (x**2)
    
def cube(x):
        return (x**3)

funcs = [square, cube]

for i in lista:
    valor = map(lambda x: x(i), funcs)
    print(list((valor)))

print('-------------------------')


# 04 CFTN:
lista = [0, 1, 2, 3, 4]

def square(x):
        return (x**2)
    
def cube(x):
        return (x**3)

funcs = [square, cube]

[print(list(map(lambda x: x(i), funcs))) for i in lista]