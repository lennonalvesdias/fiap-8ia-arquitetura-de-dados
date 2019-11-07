# ![https://www.fiap.com.br/](https://img.shields.io/badge/FIAP-red.svg?longCache=true&style=for-the-badge) MBA - Artifical Intelligence & Machine Learning

#### Cintia Akie Nakano . RM 333603 // Lennon V. Alves Dias . RM 334415 // Mateus Aguiar Florentino . RM 334444

<h1 align="center">
    Arquitetura de Dados
</h1>

<h4 align="center">
    ☕ Code and coffee
</h4>

## 💻 Aplicação

Foi desenvolvida uma aplicação em `Python` para tratar os dados obtidos pelas APIs do site [4devs.com.br](https://www.4devs.com.br/).
Essa aplicação extrai os dados necessários para o trabalho, gera distribuições aleatórias de dados faltantes de acordo com pesos, além de realizar manipulações em possíveis dados faltantes.

Uma breve defesa sobre o projeto apresentado pode ser encontrado no arquivo [REPORT.md](/REPORT.md).

## 🚀 Tecnologias

Para o desenvolvimento da API foi utilizado [Python (3.8)](https://www.python.org/), [Docker](https://docs.docker.com/) e [Neo4J](https://neo4j.com/).

### 👨‍💻 Executando a aplicação (Passo a passo)

* Clone esse repositório e navegue até ele

``` sh
$ git clone https://github.com/lennonalvesdias/fiap-8ia-arquitetura-de-dados.git

$ cd fiap-8ia-arquitetura-de-dados
```

* Inicialize o banco de dados (*requer Docker*)

``` sh
$ ./init-database.sh
```

Você pode navegar ao [localhost:7474](http://localhost:7474/) para validar seu *database* ativo e configurar sua senha de conexão.

* Instale as bibliotecas necessárias para execução da aplicação

``` sh
$ pip install -r requirements.txt
```

* Execute a aplicação para carregar a base inicial (você pode definir a quantidade de pessoas, empresas e universidades no [arquivo de execução](/app.py))

``` sh
$ ./app.py
```

* Após o término da execução, você pode navegar ao [*browser*](http://localhost:7474/) do `Neo4J` e executar as consultas entre as entidades e seus relacionamentos

## 📂 Dados

Na pasta `data` estão os arquivos extraidos da API e manipulados pela aplicação, sendo eles:

| arquivo | descrição |
|---|---|
| [`companies.txt`](/data/companies.txt) | Lista de empresas |
| [`peoples.txt`](/data/peoples.txt) | Lista de pessoas |
| [`universities.txt`](/data/universities.txt) | Lista de universidades |
