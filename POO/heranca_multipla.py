'''
Herança múltipla em Python ocorre quando uma classe herda de mais de uma classe base. 
Ou seja, uma classe filha pode ter múltiplas classes como suas "superclasses," 
herdando atributos e métodos de todas elas. Isso permite a reutilização de código e maior flexibilidade no design de classes. 

No entanto, herança múltipla pode levar a ambiguidades quando diferentes 
superclasses possuem métodos com o mesmo nome. Python resolve isso com o **C3 Linearization** 
(também conhecido como MRO - Method Resolution Order), que define a ordem de busca dos métodos.
'''

class Animal:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def emitir_som(self):
        pass

    def comer(self):
        print("nhoc nhoc")
        return "hi hi hi hi"

    def andar(self):
        print("steps")
        return "doc doc doc"

    def saudacao(self):
        print(f'Olá, este é o {self.nome}, ele é da raça {self.raca}.')

class Mamifero(Animal):
    def amamentar(self):
        print(f'{self.nome} está amamentando...')
        return "nham nham"

class Ave(Animal):
    def voar(self):
        print(f'{self.nome} está voando...')
        return "i i i i i"

class Morcego(Mamifero, Ave):    
    def emitir_som(self):
        print(f'{self.nome} está emitindo ultrassom...')
        return "US"

    def comer(self):
        super().comer()
        print(f'{self.nome} está se alimentando de frutas...')
        return "lu lu lu lu lu"

# Instanciando a classe Mamifero
macaco = Mamifero('Mico', 'Amazônico')

# Instanciando a classe Ave
papagaio = Ave('Papagaio', 'Goyases')

# Instanciando a classe Morcego
bat = Morcego('Bat', 'Vampiro')

# Acessando métodos das classes com base "Animal"
print("Nome do animal:", macaco.nome)
print("Raça do animal:", macaco.raca)
print("Macaco andando:", macaco.andar())
print("Macaco comendo:", macaco.comer())

print("Nome do animal:", papagaio.nome)
print("Raça do animal:", papagaio.raca)
print("Papagaio comendo:", papagaio.comer())
papagaio.comer()
papagaio.saudacao()

# Acessando métodos das classes com base "Mamifero" e "Ave"
print("Macaco amamentando:", macaco.amamentar())

print("Papagaio voando:", papagaio.voar())

print("Morcego amamentando:", bat.amamentar())
print("Morcego voando:", bat.voar())

# Acessando métodos da classe "Morcego"
print("Nome do morcego:", bat.nome)
print("Raça do morcego:", bat.raca)
print("Som do morcego:", bat.emitir_som())
print("Morcego comendo:", bat.comer())
