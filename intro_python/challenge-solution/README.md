# Introdução ao Python

Este repositório contém exemplos e exercícios de um projeto introdutório de Python, abordando conceitos fundamentais da linguagem. O foco está em tipos de variáveis, estruturas condicionais e de repetição, listas, tuplas, dicionários, conjuntos, tratamento de exceção e uso de módulos Python.

## Conteúdo

- [Introdução ao Python](#introdução-ao-python)
  - [Conteúdo](#conteúdo)
  - [Tipos de Variáveis](#tipos-de-variáveis)
  - [Estruturas Condicionais](#estruturas-condicionais)
  - [Estruturas de Repetição](#estruturas-de-repetição)
  - [Listas](#listas)
  - [Tuplas](#tuplas)
  - [Dicionários](#dicionários)
  - [Conjuntos](#conjuntos)
  - [Tratamento de Exceções](#tratamento-de-exceções)
  - [Módulos Python](#módulos-python)
  - [Solução do desafio pático - introdução ao Python](#solução-do-desafio-pático---introdução-ao-python)
    - [Regras da aplicação (Requisitos Funcionais)](#regras-da-aplicação-requisitos-funcionais)
    - [Estrutura de Diretórios](#estrutura-de-diretórios)
  - [Como Usar](#como-usar)
  - [Contribuindo](#contribuindo)
  - [Licença](#licença)

---

## Tipos de Variáveis

O Python é uma linguagem dinamicamente tipada, o que significa que não é necessário declarar o tipo de variável explicitamente. Alguns dos tipos primários de variáveis em Python incluem:

- **Inteiros (`int`)**: Números inteiros, ex: `x = 10`
- **Flutuantes (`float`)**: Números com ponto decimal, ex: `y = 3.14`
- **Strings (`str`)**: Sequência de caracteres, ex: `nome = "Python"`
- **Booleanos (`bool`)**: Verdadeiro ou Falso, ex: `verdadeiro = True`

## Estruturas Condicionais

O Python utiliza as palavras-chave `if`, `elif`, e `else` para estruturas de decisão.

Exemplo:

```python
x = 10
if x > 5:
    print("Maior que 5")
elif x == 5:
    print("Igual a 5")
else:
    print("Menor que 5")
```

## Estruturas de Repetição

As principais estruturas de repetição em Python são `for` e `while`.

- **For loop**: Itera sobre uma sequência (lista, tupla, dicionário, etc.)

  ```python
  for i in range(5):
      print(i)
  ```

- **While loop**: Repetição baseada em uma condição.

  ```python
  x = 0
  while x < 5:
      print(x)
      x += 1
  ```

## Listas

As listas são coleções mutáveis que podem conter elementos de diferentes tipos.

```python
lista = [1, 2, 3, "Python", True]
lista.append(4)  # Adiciona um elemento à lista
print(lista[0])  # Acessa o primeiro elemento
```

## Tuplas

Tuplas são semelhantes a listas, mas são imutáveis, ou seja, seus valores não podem ser alterados após a criação.

```python
tupla = (1, 2, 3)
print(tupla[0])  # Acessa o primeiro elemento
```

## Dicionários

Dicionários armazenam pares de chave-valor.

```python
dicionario = {"nome": "Python", "versão": 3.9}
print(dicionario["nome"])  # Acessa o valor associado à chave "nome"
dicionario["ano"] = 2021  # Adiciona um novo par chave-valor
```

## Conjuntos

Conjuntos são coleções não ordenadas de elementos únicos.

```python
conjunto = {1, 2, 3, 3}
print(conjunto)  # Saída: {1, 2, 3}
conjunto.add(4)  # Adiciona um elemento ao conjunto
```

## Tratamento de Exceções

O Python oferece um mecanismo robusto para o tratamento de exceções com `try`, `except`, e `finally`.

```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Erro: Divisão por zero")
finally:
    print("Bloco finally sempre é executado")
```

## Módulos Python

Módulos são arquivos Python que contêm definições e declarações. Eles ajudam a organizar o código em diferentes arquivos e reutilizá-los.

Para importar um módulo, usa-se a palavra-chave `import`. Python também oferece vários módulos nativos.

Exemplo:

```python
import math

print(math.sqrt(16))  # Saída: 4.0
```

Além de módulos internos como `math`, você também pode criar seus próprios módulos e importá-los da seguinte forma:

```python
# exemplo_modulo.py
def saudacao():
    return "Olá, bem-vindo ao Python!"

# arquivo principal
import exemplo_modulo

print(exemplo_modulo.saudacao())  # Saída: Olá, bem-vindo ao Python!
```

## Solução do desafio pático - introdução ao Python

Nesse desafio desenvolveremos uma agenda para salvar, editar, deletar e marcar um contato como favorito. O resultado da aplicação deve ser apresentado no terminal, assim como foi visto no módulo “Introdução ao Python”.

### Regras da aplicação (Requisitos Funcionais)

- A aplicação deve iniciar mostrando uma lista de opções do que é possível fazer com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.
- Deve ser possível adicionar um contato
  - O contato pode ter os dados:
  - Nome
  - Telefone
  - Email
  - Favorito (está opção é para poder marcar um contato como favorito)
- Deve ser possível visualizar a lista de contatos cadastrados
- Deve ser possível editar um contato
- Deve ser possível marcar/desmarcar um contato como favorito
- Deve ser possível ver uma lista de contatos favoritos
- Deve ser possível apagar um contato

### Estrutura de Diretórios

```md
src/
  ├── contacts/
  │     ├── __init__.py
  │     └── main.py
  ├── delete/
  │     ├── __init__.py
  │     └── delete.py
  ├── edit/
  │     ├── __init__.py
  │     └── edit.py
  ├── save/
  |     ├── __init__.py
  |      └── save.py
  ├── show/
  |     ├── __init__.py
  |     └── show.py
  ├── .gitignore
  └── README.md
```

## Como Usar

1. Clone o repositório;
2. Navegue até o diretório do projeto;
3. Execute os exemplos no seu ambiente Python.

---

## Contribuindo

Fique à vontade para abrir **issues** e enviar **pull requests** para melhorias no código ou na documentação.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
