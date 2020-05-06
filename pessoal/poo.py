# Criando uma classe chamada Livro
class Livro():
    
    # Este método vai inicializar cada objeto criado a partir desta classe
    # O nome deste método é __init__
    # (self) é uma referência a cada atributo de um objeto criado a partir desta classe
    def __init__(self):
        
        # Atributos de cada objeto criado a partir desta classe. 
        # O self indica que estes são atributos dos objetos
        self.titulo = 'O Monge e o Executivo'
        self.isbn = 9988888
        print("Construtor chamado para criar um objeto desta classe")
        
    # Métodos são funções, que recebem como parâmetro atributos do objeto criado    
    def imprime(self):
        print("Foi criado o livro %s e ISBN %d" %(self.titulo, self.isbn))

# Criando uma classe
class Estudantes:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

# Criando um objeto chamado Estudante1 a partir da classe Estudantes
Estudante1 = Estudantes("Pele", 12, 9.5)

# Criando uma classe chamada Circulo
class Circulo():
    
    # O valor de pi é constante
    pi = 3.14

    # Quando um objeto desta classe for criado, este método será executado e o valor default do raio será 5.
    def __init__(self, raio = 5):
        self.raio = raio 

    # Esse método calcula a área. Self utiliza os atributos deste mesmo objeto
    def area(self):
        return (self.raio * self.raio) * Circulo.pi

    # Método para gerar um novo raio
    def setRaio(self, novo_raio):
        self.raio = novo_raio

    # Método para obter o raio do círculo
    def getRaio(self):
        return self.raio

# Criando o objeto circ. Uma instância da classe Circulo()
circ = Circulo()

# Executando um método da classe Circulo
circ.getRaio()

# Criando a classe Animal - Super-classe
class Animal():
    
    def __init__(self):
        print("Animal criado")

    def Identif(self):
        print("Animal")

    def comer(self):
        print("Comendo")

# Criando a classe Cachorro - Sub-classe
class Cachorro(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Objeto Cachorro criado")

    def Identif(self):
        print("Cachorro")

    def latir(self):
        print("Au Au!")
