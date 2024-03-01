# Projeto Django de Login e Registro de Usuário

Este é um simples projeto Django que oferece funcionalidades básicas de login e registro de usuário. Quando o usuário faz login com sucesso, é redirecionado para uma página que exibe uma mensagem simples indicando que o usuário está logado.

## Instalação

1. Certifique-se de ter o Python e o Django instalados em seu ambiente de desenvolvimento. Se não tiver o Django instalado, você pode instalá-lo via pip:
    ```
    pip install django
    ```

2. Clone este repositório para o seu ambiente local:
    ```
    git clone https://github.com/cayo-cesar/django_study.git
    ```

3. Navegue até o diretório do projeto:
    ```
    cd projeto_autenticacao
    ```

4. Execute as migrações para configurar o banco de dados SQLite (ou outro banco de dados configurado em settings.py):
    ```
    python manage.py migrate
    ```

5. Inicie o servidor de desenvolvimento:
    ```
    python manage.py runserver
    ```

6. Acesse o projeto em seu navegador web em `http://localhost:8000/`.

## Funcionalidades

- Registro de novo usuário: Os usuários podem se registrar fornecendo um nome de usuário, e-mail e senha.
- Login de usuário existente: Os usuários podem fazer login usando seu nome de usuário e senha.
- Página de usuário logado: Após fazer login com sucesso, os usuários são redirecionados para uma página que exibe uma mensagem simples indicando que estão logados.
