# BiblioWebAPI - Sistema de Gerenciamento de Empréstimo de Livros

## Descrição

O **BiblioWebAPI** é um sistema desenvolvido para gerenciar o empréstimo de livros em bibliotecas públicas. Ele é construído usando o **Django** e segue as boas práticas de arquitetura **DDD (Domain-Driven Design)**, com uma estrutura modular e escalável. O projeto está configurado para ser extensível, facilitando a integração de novos contextos (como gestão de doações, acervo, etc.).

## Principais Características

- **Gestão de Empréstimos**: Registro de empréstimos de livros, com controle de prazo e devoluções.
- **Módulos Escaláveis**: Estrutura baseada em DDD, com separação clara entre camadas de domínio, aplicação, infraestrutura e apresentação.
- **Persistência de Dados**: Integração com banco de dados MySQL para persistência de dados.
- **API REST**: Fornece endpoints para interação com os dados do sistema.
- **Facilidade de Expansão**: Novo contexto e funcionalidades podem ser facilmente adicionados sem afetar o funcionamento do sistema.
- **Segurança**: Configurações de segurança como CORS, CSRF e autenticação implementadas.

## Tecnologias Utilizadas

- **Python 3.x**
- **Django 3.x**
- **MySQL**
- **Django REST Framework** (para construção da API)
- **Gunicorn** (servidor WSGI)
- **Docker** (opcional para containerização)

## Requisitos

- Python 3.8 ou superior
- MySQL 5.7 ou superior

## Como Executar o Projeto

### 1\. **Clone o Repositório**

```bash
git clone https://github.com/JulianGN/biblio.webapi.git  cd .\biblio.webapi\
```

### 2\. **Instale as Dependências**

Recomenda-se criar um ambiente virtual antes de instalar as dependências.

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### 3\. **Configuração do Banco de Dados**

Configure o banco de dados no arquivo config/database.py com as credenciais apropriadas.

```sql
CREATE DATABASE biblioDB;
```

### Configuração de Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
DATABASE_NAME=biblioDB
DATABASE_USER=seu_usuario
DATABASE_PASSWORD=sua_senha
DATABASE_HOST=localhost
DATABASE_PORT=3306
SECRET_KEY=sua_chave_secreta
DEBUG=True
```

### 4\. **Realize as Migrações**

Para configurar o banco de dados com as tabelas necessárias:

```bash
python manage.py migrate
```

### 5\. **Crie um Superusuário (opcional)**

Crie um superusuário para acessar o painel de administração do Django:

```bash
python manage.py createsuperuser
```

### 6\. **Execute o Servidor de Desenvolvimento**

Para rodar o servidor de desenvolvimento:

```bash
python manage.py runserver
```

Acesse a API em http://127.0.0.1:8000/.

### 7\. **Docker (opcional)**

Se preferir rodar o projeto em um contêiner Docker, crie a imagem com o comando:

```bash
docker-compose up --build
```

Isso iniciará o serviço em contêiner, e você poderá acessar a aplicação no localhost:8000.

## Estrutura do Projeto

```markdown
biblioWebapi/
│── src/
│ │── gestor/ # Contexto "Gestor" (Empréstimos)
│ │ │── domain/ # Entidades e regras de negócio
│ │ │── application/ # Casos de uso
│ │ │── infrastructure/ # Integração com banco, APIs externas
│ │ │── presentation/ # Controllers, Views, Serializers
│── config/ # Configurações gerais do projeto (Banco de dados, segurança)
│── manage.py # CLI do Django
│── requirements.txt # Dependências do projeto
```

## Rotas da API

A seguir estão algumas rotas da API disponíveis:

- **GET /gestor/books/** - Listar todos os livros.
- **POST /gestor/loan/** - Registrar um novo empréstimo de livro.
- **GET /gestor/loans/** - Listar todos os empréstimos.

## Problemas Comuns e Soluções

### Erro: "ModuleNotFoundError: No module named 'django'"

- Certifique-se de que o ambiente virtual está ativado.
- Instale as dependências com:
  ```bash
  pip install -r requirements.txt
  ```

## Contribuições

Contribuições são bem-vindas! Para contribuir com o projeto, siga os seguintes passos:

1.  Fork o repositório.
2.  Crie uma branch para a sua feature (git checkout -b feature/xyz).
3.  Faça o commit das suas alterações (git commit -am 'Adiciona nova feature').
4.  Push para a sua branch (git push origin feature/xyz).
5.  Abra um pull request.

## Licença

Este projeto está licenciado sob a MIT License.
