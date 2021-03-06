# Desafio_Tech-Frexco
 Repositório referente ao processo seletivo para vaga de <b>Estágio em Desenvolvimento de Software (Automação) na empresa Frexco</b>.

## Desafio Tech (Automação)
Construir pelo menos dois endpoints utilizando Django:

  [X] Cadastrar usuário, fornecendo o login, senha e data de nascimento

  [X] Senha deixar como opcional, se não fornecido gerar uma senha aleatória.

  [X] Consultar usuários cadastrados.

  [X] Deve ser possível consultar em XLSX, CSV ou JSON.

  [X] Nos enviar em um repositório publico no GitHub ou plataforma similar.

<br>

## Feito com:
 <p align="left">
 <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
 <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://static.djangoproject.com/img/logos/django-logo-positive.svg" alt="Django" width="40" height="40"/> </a>

<br>

## Requisitos:
Python

Django

<br>

# Instruções de uso:

```sh
1 - Clonar esse repositório através do git: "$ git clone https://github.com/MauPxt/desafio_tech-frexco"
2 - Acessar a pasta do repositório: "$ cd desafio_tech-frexco"
3 - Instalar os requisitos: "pip install -r requirements.txt"
4 - Iniciar o servidor:
    4.1 - "$ python manage.py makemigrations"
    4.2 - "$ python manage.py migrate"
    4.3 - "$ python manage.py runserver"
5 - Entrar no endereço da API:
    5.1 - digitar o seguinte endereço no seu navegador "http://localhost:8000/api/v1/"
6 - Realizar o login:
    6.1 - "python manage.py createsuperuser --email admin@desafiofrexco.com --username admin"
    6.2 - Introduzir no campo de usuário "admin" e no campo da senha a senha que você escolheu.
7 - Acessar o endereço "http://localhost:8000/api/v1/users/"
8 - A partir desse ponto já é possível inserir/consultar os dados da API

```