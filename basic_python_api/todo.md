# Passos para o Desenvolvimento da API Básica em Python

1. **Configurar o Ambiente de Desenvolvimento**

   - [x] Instalar Python 3.x
   - [x] Configurar um ambiente virtual
   - [x] Instalar dependências necessárias (Flask, SQLAlchemy, etc.)

2. **Estruturar o Projeto**

   - [x] Criar a estrutura de diretórios
   - [x] Configurar o arquivo `run.py`
   - [x] Criar os diretórios referentes ao padrão MVC
   - [x] Criar os diretórios de tratamento de erros
   - [x] Criar os diretórios de servidor, rotas, configs, db e drivers
   - [x] Criar o arquivo `requirements.txt`
   - [x] Criar o código para diferentes tipos de autenticação

3. **Desenvolver Endpoints Básicos**

   - [x] Criar endpoint para criar usuários (POST /user)
   - [x] Criar endpoint para listar usuários (GET /user)
   - [x] Criar endpoint para atualizar usuários (PUT /user/\<id>)
   - [x] Criar endpoint para atualizar atributo de um usuário (PATCH /user/\<id>)
   - [x] Criar endpoint para deletar usuários (DELETE /user/\<id>)

4. **Configurar Banco de Dados**

   - [x] Escolher banco de dados (SQLite, PostgreSQL, etc.)
   - [x] Configurar conexão com o banco de dados
   - [x] Criar modelos de dados com SQLAlchemy
   - [ ] Criar papeis para usuários dentro da aplicação
   - [ ] Armazenar primeiro e últimos logins
   - [ ] Criar opção de delete lógico

5. **Implementar Autenticação e Autorização**

   - [x] Configurar autenticação com JWT
   - [x] Configurar autenticação com FLASK_LOGIN
   - [x] Configurar autenticação com Firebase
   - [x] Proteger endpoints com autorização

6. **Criar Serviço de Mensageria**

   - [ ] Configurar a aplicação para WebSockets
   - [ ] Criar model de mensagens

7. **Gerar Cobrança PIX**

   - [ ] Criar conta na GerenciaNet
     - [Intro Código Fonte](https://www.youtube.com/watch?v=BRzi0rDhhCc)
     - [Demo GerenciaNet](https://www.youtube.com/watch?v=oyQ8jK24IWg)
     - [Configurar WebHook](https://www.youtube.com/watch?v=aYBgHhFDk6o)

8. **Testar a API**

   - [x] Escrever testes unitários para os endpoints
   - [x] Testar a API com ferramentas como Postman ou Insomnia

9. **Documentar a API**

   - [ ] Criar documentação dos endpoints no swagger
     - [site](https://editor.swagger.io/)
   - [ ] Incluir exemplos de requisições e respostas

10. **Deploy da API**

    - [ ] Escolher serviço de hospedagem (Heroku, AWS, etc.)
    - [ ] Configurar o deploy contínuo

11. **Manutenção e Melhorias**

    - [ ] Monitorar a API em produção
    - [ ] Implementar melhorias e novas funcionalidades conforme necessário
