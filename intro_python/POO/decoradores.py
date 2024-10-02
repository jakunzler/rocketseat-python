"""
Decoradores em Python são funções que modificam o comportamento de outras funções ou métodos, 
permitindo adicionar funcionalidades sem alterar diretamente o código da função decorada. 
Eles são amplamente usados em Python para tarefas como logging, controle de acesso, temporização de execução e muito mais.

Como Funcionam?

Um decorador é uma função que recebe outra função como argumento e retorna uma nova função, geralmente estendendo ou alterando o comportamento da função original.

Aqui está um exemplo simples de um decorador:
"""

def meu_decorador(func):
    def wrapper():
        print("Antes de executar a função")
        func()
        print("Depois de executar a função")
    return wrapper

# Agora, podemos aplicar este decorador a uma função usando o símbolo `@`:

@meu_decorador
def saudacao():
    print("Olá!")

saudacao()

"""
Aqui, a função `saudacao()` foi decorada pelo `meu_decorador`, então antes e depois de sua execução, são impressas mensagens adicionais.

Exemplo com Argumentos

Decoradores também podem funcionar com funções que aceitam argumentos:
"""

def meu_decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes da execução")
        resultado = func(*args, **kwargs)
        print("Depois da execução")
        return resultado
    return wrapper

@meu_decorador
def soma(a, b):
    return a + b

resultado = soma(3, 4)
print("Resultado:", resultado)

"""
Aqui, o decorador foi adaptado para aceitar qualquer número de argumentos, permitindo que funções como `soma` sejam decoradas.

Decoradores com Argumentos

Se quisermos que o próprio decorador aceite parâmetros, podemos criar uma função que retorna um decorador:
"""

def repetir(n):
    def decorador(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorador

@repetir(3)
def diga_oi():
    print("Oi!")

diga_oi()

"""
Neste exemplo, o decorador `@repetir(3)` faz com que a função `diga_oi` seja executada 3 vezes.

Resumo

- **Decoradores** são funções que envolvem outras funções para modificar ou estender seu comportamento.
- São úteis para adicionar funcionalidades a funções sem alterar seu código.
- A sintaxe `@decorador` é uma maneira conveniente de aplicar decoradores.
- Decoradores podem trabalhar com argumentos e até receber parâmetros.
"""