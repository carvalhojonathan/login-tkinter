# 🔐 Sistema de Login

Sistema de login com interface feita utilizando tkinter.

## 📋 Pré-requisitos

- Python 3.x 🐍
- MySQL 🐬

## 💻 Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/login-terminal.git
    ```
2. Navegue até o diretório do projeto:
    ```sh
    cd login-tkinter
    ```
3. Crie um ambiente virtual:
    ```sh
    python -m venv venv
    ```
4. Ative o ambiente virtual:
    - No Windows:
        ```sh
        venv\Scripts\activate
        ```
    - No Unix ou MacOS:
        ```sh
        source venv/bin/activate
        ```
5. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## 🚀 Uso

1. Execute o script principal:
    ```sh
    python view.py
    ```
2. Siga as instruções no terminal para fazer login ou cadastro.

## ✨ Funcionalidades

### 📝 Cadastro de Usuário

- Verificação de dados do usuário:
    - Nome deve ter entre 3 e 50 caracteres.
    - Email deve ter entre 5 e 50 caracteres.
    - Senha deve ter entre 6 e 100 caracteres.
- Cadastro de novo usuário com hash da senha.
- Verificação de email já cadastrado.

### 🔑 Login de Usuário

- Verificação de email e senha.
- Comparação de hash da senha para autenticação.
- Mensagens de sucesso ou erro no login.

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [`LICENSE`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2FUsers%2Fjonat%2FDocuments%2FGitHub%2Flogin-terminal%2FLICENSE%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "d:\Users\jonat\Documents\GitHub\login-terminal\LICENSE") para mais detalhes.

______________________________
Feito por @carvalhojonathan