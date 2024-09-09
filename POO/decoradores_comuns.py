# @classmethod
# @staticmethod

class MinhaClasse:
    contador = 0 # Atributo de classe

    def __init__(self, nome) -> None:
        self.__class__.contador += 1
        self.nome = nome # Atributo de instância
        
    def metodo_instancia(self):
        return f"Método de instância chamado para {self.nome}"

    @classmethod
    def get_contador(cls):
        return cls.contador

    @staticmethod
    def imprime():
        print('Imprime algo')
        
print(MinhaClasse.contador)
print(MinhaClasse.get_contador())

obj1 = MinhaClasse("MinhaClasse1")
print(obj1.metodo_instancia())
print(obj1.get_contador())
obj1.imprime()

obj2 = MinhaClasse("MinhaClasse2")
print(obj2.metodo_instancia())
print(obj2.get_contador())
obj2.imprime()