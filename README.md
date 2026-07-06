# Cadastro de Carro

Sistema de cadastro de veículos em Python com persistência em banco de dados MySQL.

## Funcionalidades implementadas

- CRUD de marcas:
  - Cadastrar marca
  - Listar marcas
  - Atualizar marca
  - Excluir marca

- CRUD de modelos:
  - Cadastrar modelo
  - Listar modelos
  - Atualizar modelo
  - Excluir modelo

- CRUD de carros:
  - Cadastrar carro
  - Listar carros
  - Atualizar carro
  - Excluir carro

## Atividade extra

Também foi criada uma interface gráfica simples para o sistema usando Tkinter.

A tela permite acessar:

- Cadastro de marcas;
- Cadastro de modelos;
- Cadastro de carros;
- Listagem dos registros em tabelas;
- Atualização e exclusão dos dados cadastrados.

Arquivo da interface gráfica:

```text
src/frontend.py
```

## Banco de dados

O script de criação do banco está em:

```text
sql/dump.sql
```

O banco utilizado pelo projeto se chama:

```text
concessionaria
```

## Como executar o sistema pelo terminal

1. Crie o banco de dados executando o arquivo `sql/dump.sql` no MySQL.
2. Confira os dados de conexão no arquivo `src/database.py`.
3. Instale o conector MySQL, se necessário:

```bash
pip install mysql-connector-python
```

4. Execute o sistema no modo terminal:

```bash
python src/main.py
```

## Como executar a interface gráfica

Com o banco de dados configurado, execute:

```bash
python src/frontend.py
```

A interface será aberta em uma janela com abas para Marcas, Modelos e Carros.
