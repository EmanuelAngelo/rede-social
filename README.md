# Rede Social com Django

Este projeto é uma aplicação de rede social desenvolvida com o framework Django. Ele permite que os usuários criem contas, publiquem postagens, sigam outros usuários e interajam com as postagens.

## Funcionalidades

- Registro e autenticação de usuários
- Criação, edição e exclusão de postagens
- Seguir e deixar de seguir usuários
- Curtir e comentar postagens
- Feed de postagens dos usuários seguidos

## Tecnologias Utilizadas

- Django
- SQLite (ou outro banco de dados à sua escolha)
- HTML/CSS
- JavaScript

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/rede-social.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd rede-social
    ```
3. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```
4. Ative o ambiente virtual:
    - No Windows:
        ```bash
        venv\Scripts\activate
        ```
    - No Linux/Mac:
        ```bash
        source venv/bin/activate
        ```
5. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
6. Aplique as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```
7. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

## Uso

1. Acesse `http://127.0.0.1:8000` no seu navegador.
2. Registre uma nova conta ou faça login com uma conta existente.
3. Explore as funcionalidades da rede social!

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.