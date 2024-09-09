# POO

# Classe exemplo
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f'{self.nome} está falando...')

    def comer(self):
        print(f'{self.nome} está comendo...')

    def andar(self):
        print(f'{self.nome} está andando...')
        
    def saudacao(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')
        
# Objetos
pessoa1 = Pessoa('Jonas', 35)
print('{pessoa1.nome} tem {pessoa1.idade} anos.'.format(pessoa1=pessoa1))

pessoa1.falar()
pessoa1.comer()
pessoa1.andar()
pessoa1.saudacao()