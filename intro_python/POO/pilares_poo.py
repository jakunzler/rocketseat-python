"""
01. Herança
Exemplo de herança
"""

print("\n================================")
print("Exemplo de herança")
class Animal:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def emitir_som(self):
        print(f'{self.nome} está falando...')

    def comer(self):
        print(f'{self.nome} está comendo...')

    def andar(self):
        print(f'{self.nome} está andando...')

    def saudacao(self):
        print(f'Olá, este é o {self.nome}, ele é da raça {self.raca}.')

class Cachorro(Animal):
    def __init__(self, nome, raca, cor):
        super().__init__(nome, raca)
        self.cor = cor

    def emitir_som(self):
        print(f'{self.nome} está latindo...')

    def cavar(self):
        print(f'{self.nome} está cavando...')

class Gato(Animal):
    def __init__(self, nome, raca, cor):
        super().__init__(nome, raca)
        self.cor = cor

    def emitir_som(self):
        print(f'{self.nome} está miando...')

    def subir_em_arvore(self):
        print(f'{self.nome} está subindo em árvores...')

dog = Cachorro('Rex', 'Pastor Alemão', 'Marrom')
cat = Gato('Bichano', 'Siamês', 'Branca')

"""
02. Polimorfismo
Exemplo de polimorfismo
"""

print("\n================================")
print("Exemplo de Polimorfismo")
animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} é um(a) {animal.raca} de cor {animal.cor}.")

"""
03. Encapsulamento
Exemplo de encapsulamento
"""

print("\n================================")
print("Exemplo de encapsulamento")
class ContaBancaria:
    def __init__(self, titular, saldo) -> None:
        self.__titular = titular # Atributo privado
        self.__saldo = saldo
        
    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido para depósito.")
            return 
        self.__saldo += valor
        print(f"Usuário {self.__titular} depositou o valor de R$ {valor} com sucesso.")
        
    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido para saque.")
            return
        if valor > self.__saldo:
            print("Saldo insuficiente.")
            return
        self.__saldo -= valor
        print
        
    def get_saldo(self):
        return self.__saldo
      
    def get_titular(self):
        return self.__titular
      
    def set_titular(self, titular):
        self.__titular = titular

conta = ContaBancaria(saldo = 1000, titular = 'João')
print(f"Saldo atual: R$ {conta.get_saldo()}")

conta.depositar(500)
print(f"Saldo atual: R$ {conta.get_saldo()}")

conta.depositar(-100)

conta.sacar(300)
print(f"Saldo atual: R$ {conta.get_saldo()}")

conta.sacar(1500)
print(f"Saldo atual: R$ {conta.get_saldo()}")

conta.set_titular('Maria')
print(f"Novo titular é {conta.get_titular()}")

"""
04. Abstração
Exemplo de abstração
"""

print("\n================================")
print("Exemplo de abstração")

from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def freiar(self):
        pass
      
class Carro(Veiculo):
    def acelerar(self):
        print('Acelerando...')

    def freiar(self):
        print('Freiando...')
        
class Moto(Veiculo):
    def acelerar(self):
        print('Acelerando...')

    def freiar(self):
        print('Freiando...')
        
carro = Carro()
moto = Moto()

carro.acelerar()
moto.acelerar()
carro.freiar()
moto.freiar()

print("\n================================")
print("Fim do script")
print("================================")

# End of file