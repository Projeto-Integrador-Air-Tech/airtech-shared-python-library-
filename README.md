# airtech-shared-python-library

## Descrição

O airtech-shared-python-library é um projeto de biblioteca compartilhada que oferece funcionalidades específicas, com suporte para PostgreSQL por meio de um adaptador dedicado.

## Requisitos

- Python
- PostgreSQL

## Instalação

Certifique-se de ter o Python e o PostgreSQL instalados no seu ambiente. Em seguida, execute os seguintes comandos:

```bash
pip install airtech-shared-python-library
```

## Configuração do Adaptador PostgreSQL

Para utilizar o adaptador PostgreSQL, é necessário configurar as informações de conexão. Aqui está um exemplo de como configurar o adaptador no seu código Python:

```python
from airtech_shared_python_library.adaptadores import PostgreSQLConnection

# Configuração do adaptador PostgreSQL
conexao_postgres = PostgreSQLConnection(
    host='localhost',
    port=5432,
    database='seu_banco_de_dados',
    user='seu_usuario',
    password='sua_senha'
)
```

Lembre-se de substituir as informações acima pelos detalhes específicos do seu ambiente.

## Uso do Adaptador PostgreSQL

Agora que o adaptador está configurado, você pode usá-lo para realizar consultas no banco de dados PostgreSQL. Aqui está um exemplo básico:

```python
# Exemplo de uso do adaptador PostgreSQL
with conexao_postgres as conexao:
    cursor = conexao.create_cursor()
    resultado = conexao.execute_query("SELECT * FROM sua_tabela;")
    for linha in resultado.fetchall():
        print(linha)
```

## Contribuição

Se você quiser contribuir para este projeto, siga estas etapas:

- Fork do projeto
- Crie uma nova branch (git checkout -b feature/nova-feature)
- Faça commit das suas alterações (git commit -m 'Adicionar nova feature')
- Faça push para a branch (git push origin feature/nova-feature)
- Abra um pull request
