# Cadastro de Carro

Sistema simples de cadastro de veículos em Python com persistência em banco de dados MySQL.

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

## Banco de dados

O script de criação do banco está em:

```text
sql/dump.sql
```

O banco utilizado pelo projeto se chama:

```text
concessionaria
```

## Como executar

1. Crie o banco de dados executando o arquivo `sql/dump.sql` no MySQL.
2. Confira os dados de conexão no arquivo `src/database.py`.
3. Instale o conector MySQL, se necessário:

```bash
pip install mysql-connector-python
```

4. Execute o sistema:

```bash
python src/main.py
```
