# Aplicação FastAPI CRUD

Este projeto é uma aplicação FastAPI com operações básicas de CRUD (Criar, Ler, Atualizar, Deletar) integradas ao PostgreSQL usando SQLAlchemy. A aplicação é containerizada usando Docker, o que facilita a configuração e implantação.

## Índice

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Endpoints da API](#endpoints-da-api)
- [Configuração do Banco de Dados](#configuração-do-banco-de-dados)
- [Desenvolvimento](#desenvolvimento)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

---

## Visão Geral

Este projeto demonstra o uso de FastAPI com PostgreSQL para gerenciar dados de usuários através de uma API RESTful. A aplicação é totalmente containerizada usando Docker e Docker Compose, permitindo fácil desenvolvimento e implantação.

## Funcionalidades

- Operações CRUD para usuários.
- Framework FastAPI para desenvolvimento de aplicações web assíncronas.
- Integração com o banco de dados PostgreSQL usando SQLAlchemy.
- Docker e Docker Compose para desenvolvimento e implantação containerizados.
- Mecanismo de verificação de integridade (healthcheck) para o serviço PostgreSQL.

## Pré-requisitos

Antes de começar, certifique-se de ter atendido aos seguintes requisitos:

- **Docker** (versão 24.x ou posterior)
- **Docker Compose** (versão 1.29.x ou posterior)
- **Python** (versão 3.9 ou posterior)

## Instalação

### 1. Clone o repositório:

comando> git clone https://github.com/seuusuario/fastapi-crud.git  
comando> cd fastapi-crud

### 2. Construa e execute os containers Docker:

comando> docker-compose up --build

Este comando irá:
- Construir os containers FastAPI e PostgreSQL.
- Expor a API em `localhost:8000`.

### 3. Verifique se os serviços estão rodando:

Você pode verificar se a aplicação está rodando acessando:

http://localhost:8000/


## Uso

### Interagindo com a API

Após a execução da aplicação, você pode interagir com a API usando `curl`, Postman ou diretamente pelo navegador.

### Exemplos de Requisições

**Criar um usuário:**

comando> POST /usuarios/

**Obter todos os usuários:**

comando> GET /usuarios/

**Obter um usuário específico:**

comando> GET /usuarios/{user_id}

**Atualizar um usuário:**

comando> PUT /usuarios/{user_id}

**Deletar um usuário:**

comando> DELETE /usuarios/{user_id}

---

## Endpoints da API

| Método | Endpoint             | Descrição                    |
|--------|----------------------|------------------------------|
| GET    | `/usuarios/`          | Listar todos os usuários      |
| GET    | `/usuarios/{id}`      | Obter usuário por ID          |
| POST   | `/usuarios/`          | Criar um novo usuário         |
| PUT    | `/usuarios/{id}`      | Atualizar um usuário pelo ID  |
| DELETE | `/usuarios/{id}`      | Deletar um usuário pelo ID    |

---

## Configuração do Banco de Dados

O container PostgreSQL é configurado automaticamente com as seguintes variáveis de ambiente:

comando> POSTGRES_USER=vusht  
comando> POSTGRES_PASSWORD=150220  
comando> POSTGRES_DB=fastapi_db

O banco de dados é inicializado automaticamente quando os containers são iniciados.

---

## Desenvolvimento

### Executando localmente sem Docker

Para rodar a aplicação sem Docker, siga os passos abaixo:

1. Crie um ambiente virtual:

   comando> python3 -m venv venv  
   comando> source venv/bin/activate

2. Instale as dependências:

   comando> pip install -r requirements.txt

3. Inicie o servidor FastAPI:

   comando> uvicorn app.main:app --reload

### Executando Testes

Para rodar os testes unitários, use o seguinte comando:

comando> pytest

---

## Contribuindo

Contribuições são bem-vindas! Siga os seguintes passos para contribuir:

1. Faça um fork do repositório.
2. Crie uma nova branch (`git checkout -b feature-branch`).
3. Faça suas alterações e faça o commit (`git commit -m 'Adiciona uma nova funcionalidade'`).
4. Envie sua branch (`git push origin feature-branch`).
5. Abra um pull request.

---

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## Contato

Para mais informações, entre em contato:

- **Mantenedor do Projeto**: [Seu Nome](https://github.com/seuusuario)

---

### Recursos Adicionais

- Documentação do FastAPI: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
- Documentação do Docker: [https://docs.docker.com/](https://docs.docker.com/)
- Documentação do PostgreSQL: [https://www.postgresql.org/docs/](https://www.postgresql.org/docs/)



