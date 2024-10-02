# Personagem: classe mãe
# Heroi: controlado pelo usuário
# Inimigo: adversário do usuário

class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel
        
    def get_nome(self):
        return self.__nome
      
    def get_vida(self):
        return self.__vida
      
    def get_nivel(self):
        return self.__nivel
    
    def atacar(self, alvo):
        dano = self.__nivel * 2
        alvo.receber_ataque(dano)
        print(f"{self.__nome} atacou {alvo.get_nome()} e causou {dano} de dano!")
        
    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0
        # print(f"{self.__nome} recebeu {dano} de dano!")

    def __str__(self) -> str:
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNivel: {self.get_nivel()}"
      
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade
        
    def get_habilidade(self):
        return self.__habilidade
    
    def ataque_especial(self, alvo):
        dano = self.get_nivel() * 5
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} usou a habilidade {self.get_habilidade()} e causou {dano} de dano!")
      
    def __str__(self) -> str:
        return super().__str__() + f"\nHabilidade: {self.get_habilidade()}"
            
class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
        
    def get_tipo(self):
        return self.__tipo
      
    def __str__(self) -> str:
        return super().__str__() + f"\nTipo: {self.get_tipo()}"

class Jogo:
    """
    Classe orquestradora do jogo
    """
    
    def __init__(self, heroi, inimigo):
        self.__heroi = heroi
        self.__inimigo = inimigo
        
    def __str__(self) -> str:
        return f"{self.__heroi}\n\n{self.__inimigo}"
    
    def iniciar_batalha(self):
        """
        Fazer a gestão da batlha em turnos
        """
        print("Batalha iniciada!")
        while self.__heroi.get_vida() > 0 and self.__inimigo.get_vida() > 0:
            print("\nDetalhes dos Personagens:")
            print("Turno do heroi")
            print(heroi)
            print("Turno do inimigo")
            print(inimigo)
            
            input("Pressione Enter para continuar...")
            escolha = input("Escolha sua ação:\n[1] Ataque Normal\n[2] Ataque Especial\nEscolha: ")
            
            if escolha == "1":
                self.__heroi.atacar(self.__inimigo)
            elif escolha == "2":
                self.__heroi.ataque_especial(self.__inimigo)
            else:
                print("Escolha inválida. Tente novamente...")
                
            if self.__inimigo.get_vida() > 0:
                # Inimigo ataca o herói
                self.__inimigo.atacar(self.__heroi)

        if self.__heroi.get_vida() > 0:
            print("Você venceu!")
        else:
            print("Você perdeu!")

heroi = Heroi(nome="Heroi", vida=100, nivel=5, habilidade="Super Força")
inimigo = Inimigo(nome="Morcego", vida=50, nivel=3, tipo="voador")

jogo = Jogo(heroi, inimigo)
print(jogo)
jogo.iniciar_batalha()