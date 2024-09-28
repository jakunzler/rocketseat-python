# Instructions

Estrutura de pastas para o projeto de API com Flask, seguindo o padrão MVC e boas práticas de organização PEP8.

## Constução do projeto

### Estrutura de Pastas

```plaintext
project_root/
│
├── app/
│   ├── __init__.py                # Inicialização do app Flask
│   ├── models.py                  # Definição dos modelos de dados (User, UserSession, etc.)
│   ├── controllers.py             # Lógica de negócios e controle (ex: autenticação)
│   ├── routes.py                  # Definição das rotas da API
│   ├── utils.py                   # Utilitários (ex: criptografia, geração de JWT)
│   └── schemas.py                 # Esquemas de validação (com Pydantic, Marshmallow, etc.)
│
├── config.py                      # Configurações do app (ex: variáveis de ambiente, chaves secretas)
├── requirements.txt               # Dependências do projeto (para instalar com pip)
├── run.py                         # Arquivo para rodar o servidor Flask
├── .env                           # Arquivo para guardar variáveis de ambiente (não deve ser commitado)
├── migrations/                    # Diretório para arquivos de migração do banco de dados (caso use Flask-Migrate)
│
└── tests/                         # Testes automatizados (unitários, integração, etc.)
    └── test_app.py                # Arquivo de testes da aplicação
```

### Passo a Passo para Configurar o Projeto com Flask

1. **Criação do Ambiente Virtual e Instalação de Dependências**

    Crie e ative um ambiente virtual Python (opcional, mas recomendado):

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # Linux/Mac
    # .\venv\Scripts\activate  # Windows
    ```

    Instale as dependências básicas do arquivo `requirements.txt`:

    ```bash
    pip install -r .\requirements.txt
    ```

2. **Banco de Dados**

    Para criar o banco de dados e executar as migrações, rode:

    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

3. Definir a variável de ambiente FLASK_APP:

    Para que o Flask saiba qual aplicativo carregar, é preciso definir a variável de ambiente FLASK_APP. Executar o seguinte comando para especificar o ponto de entrada correto (assumindo que o arquivo principal seja run.py):

    No Windows (CMD):

    ```cmd
    set FLASK_APP=run.py
    ```

    ```powershell
    $env:FLASK_APP = "run.py"
    ```

    ```bash
    export FLASK_APP=run.py
    ```

4. **Rodando o Projeto**

    Agora, com a estrutura organizada e o servidor Flask configurado, inicie o projeto rodando o seguinte comando:

    ```bash
    python run.py
    ```
