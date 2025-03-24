BiblioWebAPI - Sistema de Gerenciamento de Empréstimo de Livros
===============================================================

Descrição
---------

O **BiblioWebAPI** é um sistema desenvolvido para gerenciar o empréstimo de livros em bibliotecas públicas. Ele é construído usando o **Django** e segue as boas práticas de arquitetura **DDD (Domain-Driven Design)**, com uma estrutura modular e escalável. O projeto está configurado para ser extensível, facilitando a integração de novos contextos (como gestão de doações, acervo, etc.).

Principais Características
--------------------------

*   **Gestão de Empréstimos**: Registro de empréstimos de livros, com controle de prazo e devoluções.
    
*   **Módulos Escaláveis**: Estrutura baseada em DDD, com separação clara entre camadas de domínio, aplicação, infraestrutura e apresentação.
    
*   **Persistência de Dados**: Integração com banco de dados MySQL para persistência de dados.
    
*   **API REST**: Fornece endpoints para interação com os dados do sistema.
    
*   **Facilidade de Expansão**: Novo contexto e funcionalidades podem ser facilmente adicionados sem afetar o funcionamento do sistema.
    
*   **Segurança**: Configurações de segurança como CORS, CSRF e autenticação implementadas.
    

Tecnologias Utilizadas
----------------------

*   **Python 3.x**
    
*   **Django 3.x**
    
*   **MySQL**
    
*   **Django REST Framework** (para construção da API)
    
*   **Gunicorn** (servidor WSGI)
    
*   **Docker** (opcional para containerização)
    

Requisitos
----------

*   Python 3.8 ou superior
    
*   MySQL 5.7 ou superior
    

Como Executar o Projeto
-----------------------

### 1\. **Clone o Repositório**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopiarEditargit clone https://github.com/usuário/biblioWebAPI.git  cd biblioWebAPI   `

### 2\. **Instale as Dependências**

Recomenda-se criar um ambiente virtual antes de instalar as dependências.

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopiarEditarpython3 -m venv venv  source venv/bin/activate  # Linux/macOS  venv\Scripts\activate     # Windows  pip install -r requirements.txt   `

### 3\. **Configuração do Banco de Dados**

*   sqlCopiarEditarCREATE DATABASE biblioDB;
    
*   Configure o banco de dados no arquivo config/database.py com as credenciais apropriadas.
    

### 4\. **Realize as Migrações**

Para configurar o banco de dados com as tabelas necessárias:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopiarEditarpython manage.py migrate   `

### 5\. **Crie um Superusuário (opcional)**

Crie um superusuário para acessar o painel de administração do Django:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopiarEditarpython manage.py createsuperuser   `

### 6\. **Execute o Servidor de Desenvolvimento**

Para rodar o servidor de desenvolvimento:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopiarEditarpython manage.py runserver   `

Acesse a API em http://127.0.0.1:8000/.

### 7\. **Docker (opcional)**

Se preferir rodar o projeto em um contêiner Docker, crie a imagem com o comando:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopiarEditardocker-compose up --build   `

Isso iniciará o serviço em contêiner, e você poderá acessar a aplicação no localhost:8000.

Estrutura do Projeto
--------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopiarEditarbiblioWebapi/  │── src/  │   │── gestor/         # Contexto "Gestor" (Empréstimos)  │   │   │── domain/     # Entidades e regras de negócio  │   │   │── application/ # Casos de uso  │   │   │── infrastructure/ # Integração com banco, APIs externas  │   │   │── presentation/ # Controllers, Views, Serializers  │── config/             # Configurações gerais do projeto (Banco de dados, segurança)  │── manage.py           # CLI do Django  │── requirements.txt    # Dependências do projeto   `

Rotas da API
------------

A seguir estão algumas rotas da API disponíveis:

*   **GET /gestor/books/** - Listar todos os livros.
    
*   **POST /gestor/loan/** - Registrar um novo empréstimo de livro.
    
*   **GET /gestor/loans/** - Listar todos os empréstimos.
    

Contribuições
-------------

Contribuições são bem-vindas! Para contribuir com o projeto, siga os seguintes passos:

1.  Fork o repositório.
    
2.  Crie uma branch para a sua feature (git checkout -b feature/xyz).
    
3.  Faça o commit das suas alterações (git commit -am 'Adiciona nova feature').
    
4.  Push para a sua branch (git push origin feature/xyz).
    
5.  Abra um pull request.
    

Licença
-------

Este projeto está licenciado sob a MIT License.
