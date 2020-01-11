# Teste de Consulta Arquivei

Projeto desenvolvido para processo seletivo da empresa Arquivei. Este projeto possui um endpoint para consulta de notas 
já cadastradas e uma integração a API da Arquivei para alimentação do banco.

## Iniciando

Fazer o clone do projeto para máquina local

### Pré-requisitos
- MySql Server
- Insomnia (ou aplicação de testes de requisição similar)
- Python 3
- Pip

### Instalação
Para executar em máquina local:

Instalar pelo terminal o arquivo de requirements:

```
pip install --upgrade -r requirements.txt
```

Para executar via docker, apenas execute o dockerfile

### Execução

- O script com a criação do banco esperado para a execução deste projeto se encontra no arquivo create_db.
- Para a atualização do banco com os dados da API da Arquivei, executar o arquivo main.py de um terminal.

```
python main.py
```

- Para ativar o Endpoint e realizar consultas na base da aplicação, executar o arquivo app.py

```
python app.py
```

Na aplicação de requisições escolhida, envie a requisição da seguinte maneira:

```
 http://127.0.0.1:5000/notes/[número da chave de acesso]
```

### Pacotes

- Connections:
Este pacote possui a classe de conexão e controle do banco de dados.
Como este código foi desenvolvimento apenas para execução local, os dados do banco se encontram hardcoded nesta classe e
não em um cofre de acesso restrito (Como SSM). Os métodos de inserção e seleção se encontram desacoplados para 
re-utilização e fácil manutenção.

- Design_patterns:
Aqui existe uma classe abstrata Singleton, para implementação em outras classes.

- Logs:
Classe para impressão e escrita de arquivo de logs. Implementação de Singleton.

- Utils:
Classes de consulta e criptografia, este pacote fará a requisição para a API da arquivei com as chaves fornecidas e irá 
validar a resposta antes da inserção no banco. A classe criptografia possue os métodos de criptografia e descriptografia 
com a chave configurada no arquivo settings.py

- app.py:
Classe Rest para consulta. A mesma fará uma varredura no banco de todas as chaves e irá comparar com a chave informada 
pela requisição. Implementada aqui de forma a atender um pequeno banco de teste. Caso haja a necessidade, uma busca 
focada será mais eficaz.

- main.py:
Classe que irá controlar a busca e inserção das chaves resgatadas da API Arquivei.

### Outros

- Todas as informações são criptografadas antes de transitar para o banco e são descriptografadas para leitura.
- O controlador do DB é Singleton para evitar diversas instâncias e conexões com o banco.

### Testes
- Testes unitários:
Executar arquivo tests.py

```
python tests.py
```

### Melhorias
Para as próximas versões:
- Verificação de chaves duplicadas antes da inserção em banco.


## Autor

**Daniel Pacheco** 
